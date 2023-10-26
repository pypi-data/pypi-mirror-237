from dataclasses import asdict
import json
import time
import uuid
from datetime import datetime
from types import TracebackType
from typing import Any, Callable, cast
from typing_extensions import Self  # available in `typing` in 3.11+
from urllib.parse import urlparse
from websockets.sync.client import connect as ws_connect, ClientConnection
from h2ogpte.types import (
    ChatAcknowledgement,
    ChatError,
    ChatMessage,
    ChatRequest,
    ChatResponse,
    PartialChatMessage,
    SessionError,
)


class Session:
    def __init__(self, address: str, api_key: str, chat_session_id: str):
        url = urlparse(address)
        scheme = "wss" if url.scheme == "https" else "ws"
        # TODO handle base URLs
        self._address = f"{scheme}://{url.netloc}/ws"
        self._api_key = api_key
        self._chat_session_id = chat_session_id
        self._connection: ClientConnection | None = None

    @property
    def connection(self) -> ClientConnection:
        if not self._connection:
            raise RuntimeError("Session was not properly connect()ed")
        return self._connection

    def connect(self):
        self._connection = ws_connect(
            self._address,
            additional_headers={"Authorization": f"Bearer {self._api_key}"},
        )

    def query(
        self,
        message: str,
        system_prompt: str | None = None,
        pre_prompt_query: str | None = None,
        prompt_query: str | None = None,
        pre_prompt_summary: str | None = None,
        prompt_summary: str | None = None,
        llm: str | int | None = None,
        llm_args: dict[str, Any] | None = None,
        timeout: float | None = None,
        callback: Callable[[ChatMessage | PartialChatMessage], None] | None = None,
    ) -> ChatMessage | None:
        correlation_id = str(uuid.uuid4())
        request = ChatRequest(
            t="cq",
            mode="s",
            session_id=self._chat_session_id,
            correlation_id=correlation_id,
            body=message,
            system_prompt=system_prompt,
            pre_prompt_query=pre_prompt_query,
            prompt_query=prompt_query,
            pre_prompt_summary=pre_prompt_summary,
            prompt_summary=prompt_summary,
            llm=llm,
            llm_args=json.dumps(llm_args) if llm_args else None,
        )
        self.connection.send(serialize(request))

        if timeout is None:
            timeout = 1000
        deadline = time.time() + timeout
        request_id: str | None = None
        while True:
            res = self.connection.recv(deadline - time.time())
            assert isinstance(res, str)
            payloads = res.splitlines()
            for payload in payloads:
                res = deserialize(payload)
                if res.t == "cx":  # ack
                    if res.session_id != self._chat_session_id:
                        continue
                    if res.correlation_id == correlation_id:
                        request_id = res.message_id
                elif res.t == "ca":  # response
                    if (
                        res.session_id != self._chat_session_id
                        or res.reply_to_id != request_id
                    ):
                        continue
                    chat_message = ChatMessage(
                        id=res.message_id,
                        content=res.body,
                        reply_to=res.reply_to_id,
                        votes=0,
                        created_at=datetime.now(),
                    )
                    if callback:
                        callback(chat_message)
                        return
                    else:
                        return chat_message
                elif res.t == "cp":  # partial response
                    if callback:
                        if (
                            res.session_id != self._chat_session_id
                            or res.reply_to_id != request_id
                        ):
                            continue
                        callback(
                            PartialChatMessage(
                                id=res.message_id,
                                content=res.body,
                                reply_to=res.reply_to_id,
                            )
                        )
                elif res.t == "ce":
                    if (
                        res.session_id != self._chat_session_id
                        or res.reply_to_id != request_id
                    ):
                        continue
                    raise SessionError(f"Remote error: {res.body}")

    def disconnect(self):
        self.connection.close()

    def __enter__(self) -> Self:
        self.connect()
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.disconnect()


def serialize(request: ChatRequest) -> str:
    return json.dumps(asdict(request), allow_nan=False, separators=(",", ":"))


def deserialize(response: str) -> ChatResponse | ChatAcknowledgement | ChatError:
    data = cast(dict[str, Any], json.loads(response))
    t = data["t"]
    if t == "cx":
        return ChatAcknowledgement(**data)
    elif t == "ca" or t == "cp":
        return ChatResponse(**data)
    elif t == "ce":
        return ChatError(**data)
    else:
        raise SessionError(f"Invalid chat response type: {t}.")

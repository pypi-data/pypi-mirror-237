import json
import requests
import time
from typing import Iterable, Any
from h2ogpte.session import Session

from h2ogpte.types import (
    Answer,
    ChatMessage,
    ChatMessageReference,
    ChatSessionCount,
    ChatSessionForCollection,
    ChatSessionInfo,
    Chunk,
    Chunks,
    Collection,
    CollectionCount,
    CollectionInfo,
    Document,
    DocumentCount,
    DocumentInfo,
    ExtractionAnswer,
    Identifier,
    InvalidArgumentError,
    Job,
    Meta,
    ObjectCount,
    ObjectNotFoundError,
    Result,
    SchedulerStats,
    SearchResult,
    SearchResults,
    SessionError,
)


class H2OGPTE:
    def __init__(self, address: str, api_key: str):
        # Remove trailing slash from address, if any
        address = address.rstrip("/ ")

        self._address = address
        self._api_key = api_key
        self._auth_header = f"Bearer {self._api_key}"

    def _get(self, slug: str):
        res = requests.get(
            f"{self._address}{slug}",
            headers={
                "Content-Type": "application/json",
                "Authorization": self._auth_header,
            },
        )
        if res.status_code != 200:
            raise Exception(f"HTTP error: {res.status_code} {res.reason}")
        return unmarshal(res.text)

    def _post(self, slug: str, data: Any):
        res = requests.post(
            f"{self._address}{slug}",
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": self._auth_header,
            },
        )
        if res.status_code != 200:
            if res.status_code == 404:
                raise ObjectNotFoundError(
                    f"Object not found. {res.content.decode('utf-8')}"
                )
            if res.status_code == 400:
                raise InvalidArgumentError(
                    f"Invalid argument type. {res.content.decode('utf-8')}"
                )
            if res.status_code == 500:
                raise Exception(f"{res.content.decode('utf-8')}")
            else:
                raise Exception(
                    f"HTTP error: {res.status_code} {res.content.decode('utf-8')}"
                )
        return unmarshal(res.text)

    def _db(self, method: str, *args):
        return self._post("/rpc/db", marshal([method, *args]))

    def _job(self, method: str, **kwargs):
        return self._post("/rpc/job", marshal([method, kwargs]))

    def _lang(self, method: str, **kwargs):
        res = self._post("/rpc/lang", marshal(dict(method=method, params=kwargs)))
        err = res.get("error")
        if err:
            raise Exception(err)
        return res["result"]

    def _vex(self, method: str, collection_id: str, **kwargs):
        return self._post(
            "/rpc/vex",
            marshal(dict(method=method, collection_id=collection_id, params=kwargs)),
        )

    def _wait(self, d):
        job_id = _to_id(d)
        while True:
            time.sleep(1)
            job = self.get_job(job_id)
            if job.completed or job.canceled:
                break
        return job

    def answer_question(
        self,
        question: str | None = None,
        system_prompt: str = "",  # '' to disable, 'auto' to use LLMs default
        text_context_list: list[str] | None = None,
        llm: str | int | None = None,
        llm_args: dict[str, Any] | None = None,
        chat_conversation: list[tuple[str, str]] | None = None,
        **kwargs,
    ):
        ret = self._lang(
            "answer_question_using_context",
            prompt=question,
            system_prompt=system_prompt,
            text_context_list=text_context_list,
            llm=llm,
            llm_args=llm_args,
            chat_conversation=chat_conversation,
            **kwargs,
        )
        assert isinstance(ret, dict)
        for key in ret:
            assert key in ["content", "error"]
        if ret["error"]:
            raise SessionError(ret["error"])
        return Answer(**ret)

    def summarize_content(
        self,
        text_context_list: list[str] | None = None,
        system_prompt: str = "",  # '' to disable, 'auto' to use LLMs default
        pre_prompt_summary: str | None = None,
        prompt_summary: str | None = None,
        llm: str | int | None = None,
        llm_args: dict[str, Any] | None = None,
        **kwargs,
    ):
        return Answer(
            **self._lang(
                "create_summary_from_context",
                text_context_list=text_context_list,
                system_prompt=system_prompt,
                pre_prompt_summary=pre_prompt_summary,
                prompt_summary=prompt_summary,
                llm=llm,
                llm_args=llm_args,
                **kwargs,
            )
        )

    def extract_data(
        self,
        text_context_list: list[str] | None = None,
        system_prompt: str = "",  # '' to disable, 'auto' to use LLMs default
        pre_prompt_extract: str | None = None,
        prompt_extract: str | None = None,
        llm: str | int | None = None,
        llm_args: dict[str, Any] | None = None,
        **kwargs,
    ):
        return ExtractionAnswer(
            **self._lang(
                "extract_data_from_context",
                text_context_list=text_context_list,
                system_prompt=system_prompt,
                pre_prompt_extract=pre_prompt_extract,
                prompt_extract=prompt_extract,
                llm=llm,
                llm_args=llm_args,
                **kwargs,
            )
        )

    def cancel_job(self, job_id: str) -> Result:
        return Result(**self._job(".Cancel", job_id=job_id))

    def count_chat_sessions(self) -> int:
        return ChatSessionCount(**self._db("count_chat_sessions")).chat_session_count

    def count_chat_sessions_for_collection(self, collection_id: str) -> int:
        return ChatSessionCount(
            **self._db("count_chat_sessions_for_collection", collection_id)
        ).chat_session_count

    def count_collections(self) -> int:
        return CollectionCount(**self._db("count_collections")).collection_count

    def count_documents(self) -> int:
        return DocumentCount(**self._db("count_documents")).document_count

    def count_documents_in_collection(self, collection_id: str) -> int:
        return DocumentCount(
            **self._db("count_documents_in_collection", collection_id)
        ).document_count

    def count_assets(self) -> ObjectCount:
        return ObjectCount(**self._db("count_assets"))

    def create_chat_session(self, collection_id: str) -> str:
        return _to_id(self._db("create_chat_session", collection_id))

    def create_collection(self, name: str, description: str) -> str:
        return _to_id(self._db("create_collection", name, description))

    def delete_chat_sessions(self, chat_session_ids: Iterable[str]) -> Result:
        return Result(**self._db("delete_chat_sessions", chat_session_ids))

    def delete_collections(self, collection_ids: Iterable[str]):
        return self._wait(
            self._job("crawl.DeleteCollectionsJob", collection_ids=collection_ids)
        )

    def delete_documents(self, document_ids: Iterable[str]):
        return self._wait(
            self._job("crawl.DeleteDocumentsJob", document_ids=document_ids)
        )

    def delete_documents_from_collection(
        self, collection_id: str, document_ids: Iterable[str]
    ):
        return self._wait(
            self._job(
                "crawl.DeleteDocumentsFromCollectionJob",
                collection_id=collection_id,
                document_ids=document_ids,
            )
        )

    def encode_for_retrieval(self, chunks: list[str]) -> list[list[float]]:
        return self._lang("encode_for_retrieval", chunks=chunks)

    def get_chunks(self, collection_id: str, chunk_ids: Iterable[int]) -> list[Chunk]:
        res = self._vex("get_chunks", collection_id, chunk_ids=list(chunk_ids))
        return Chunks(**res).result

    def get_collection(self, collection_id: str) -> Collection:
        res = self._db("get_collection", collection_id)
        if len(res) == 0:
            raise ObjectNotFoundError(f"Collection {collection_id} not found")
        return Collection(**res[0])

    def get_collection_for_chat_session(self, chat_session_id: str) -> Collection:
        res = self._db("get_collection_for_chat_session", chat_session_id)
        if len(res) == 0:
            raise ObjectNotFoundError(f"Collection not found")
        return Collection(**res[0])

    def get_document(self, document_id: str) -> Document:
        res = self._db("get_document", document_id)
        if len(res) == 0:
            raise ObjectNotFoundError(f"Document {document_id} not found")
        return Document(**res[0])

    def get_job(self, job_id: str) -> Job:
        res = self._job(".Get", job_id=job_id)
        if len(res) == 0:
            raise ObjectNotFoundError(f"Job {job_id} not found")
        return Job(**(res[0]))

    def get_meta(self) -> Meta:
        return Meta(**(self._get("/rpc/meta")))

    def get_scheduler_stats(self) -> SchedulerStats:
        return SchedulerStats(**self._job(".Stats"))

    def ingest_from_file_system(self, collection_id: str, root_dir: str, glob: str):
        return self._wait(
            self._job(
                "crawl.IngestFromFileSystemJob",
                collection_id=collection_id,
                root_dir=root_dir,
                glob=glob,
            )
        )

    def ingest_uploads(self, collection_id: str, upload_ids: Iterable[str]):
        return self._wait(
            self._job(
                "crawl.IngestUploadsJob",
                collection_id=collection_id,
                upload_ids=upload_ids,
            )
        )

    def ingest_website(self, collection_id: str, url: str):
        return self._wait(
            self._job("crawl.IngestWebsiteJob", collection_id=collection_id, url=url)
        )

    def list_chat_messages(
        self, chat_session_id: str, offset: int, limit: int
    ) -> list[ChatMessage]:
        return [
            ChatMessage(**d)
            for d in self._db("list_chat_messages", chat_session_id, offset, limit)
        ]

    def list_chat_message_references(
        self, message_id: str
    ) -> list[ChatMessageReference]:
        return [
            ChatMessageReference(**d)
            for d in self._db("list_chat_message_references", message_id)
        ]

    def list_chat_sessions_for_collection(
        self, collection_id: str, offset: int, limit: int
    ) -> list[ChatSessionForCollection]:
        return [
            ChatSessionForCollection(**d)
            for d in self._db(
                "list_chat_sessions_for_collection", collection_id, offset, limit
            )
        ]

    def list_collections_for_document(
        self, document_id: str, offset: int, limit: int
    ) -> list[CollectionInfo]:
        return [
            CollectionInfo(**d)
            for d in self._db(
                "list_collections_for_document", document_id, offset, limit
            )
        ]

    def list_documents_in_collection(
        self, collection_id: str, offset: int, limit: int
    ) -> list[DocumentInfo]:
        return [
            DocumentInfo(**d)
            for d in self._db(
                "list_documents_in_collection", collection_id, offset, limit
            )
        ]

    def list_jobs(self) -> list[Job]:
        return [Job(**d) for d in self._job(".list")]

    def list_recent_chat_sessions(
        self, offset: int, limit: int
    ) -> list[ChatSessionInfo]:
        return [
            ChatSessionInfo(**d)
            for d in self._db("list_recent_chat_sessions", offset, limit)
        ]

    def list_recent_collections(self, offset: int, limit: int) -> list[CollectionInfo]:
        return [
            CollectionInfo(**d)
            for d in self._db("list_recent_collections", offset, limit)
        ]

    def list_recent_documents(self, offset: int, limit: int) -> list[DocumentInfo]:
        return [
            DocumentInfo(**d) for d in self._db("list_recent_documents", offset, limit)
        ]

    def match_chunks(
        self,
        collection_id: str,
        vectors: list[list[float]],
        topics: list[str],
        offset: int,
        limit: int,
        cut_off: float = 0,
        width: int = 0,
    ) -> list[SearchResult]:
        res = self._vex(
            "match_chunks",
            collection_id,
            vectors=vectors,
            topics=topics,
            offset=offset,
            limit=limit,
            cut_off=cut_off,
            width=width,
        )
        return SearchResults(**res).result

    def search_chunks(
        self, collection_id: str, query: str, topics: list[str], offset: int, limit: int
    ) -> list[SearchResult]:
        res = self._vex(
            "search_chunks",
            collection_id,
            query=query,
            topics=topics,
            offset=offset,
            limit=limit,
        )
        return SearchResults(**res).result

    def set_chat_message_votes(self, chat_message_id: str, votes: int) -> Result:
        return Result(**self._db("set_chat_message_votes", chat_message_id, votes))

    def update_collection(self, collection_id: str, name: str, description: str) -> str:
        return _to_id(self._db("update_collection", collection_id, name, description))

    def upload(self, file_name: str, file: Any) -> str:
        res = requests.post(
            f"{self._address}/rpc/fs",
            headers={
                "Authorization": self._auth_header,
            },
            files=dict(file=(file_name, file)),
        )
        if res.status_code != 200:
            raise Exception(f"HTTP error: {res.status_code} {res.reason}")
        return _to_id(unmarshal(res.text))

    def connect(self, chat_session_id: str) -> Session:
        return Session(
            self._address, api_key=self._api_key, chat_session_id=chat_session_id
        )

    def get_llms(self) -> list[dict]:
        return self._lang("get_llms")


def _to_id(data: dict) -> str:
    return Identifier(**data).id


def marshal(d):
    return json.dumps(d, allow_nan=False, separators=(",", ":"))


def unmarshal(s: str):
    return json.loads(s)

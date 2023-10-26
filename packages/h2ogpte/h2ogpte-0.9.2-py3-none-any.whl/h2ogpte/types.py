from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import Literal


class Status(str, Enum):
    Unknown = "unknown"
    Scheduled = "scheduled"
    Queued = "queued"
    Running = "running"
    Completed = "completed"
    Failed = "failed"
    Canceled = "canceled"


class Answer(BaseModel):
    content: str
    error: str


class ExtractionAnswer(BaseModel):
    content: list[str]
    error: str


class ChatMessage(BaseModel):
    id: str
    content: str
    reply_to: str | None
    votes: int
    created_at: datetime


class PartialChatMessage(BaseModel):
    id: str
    content: str
    reply_to: str | None


class ChatMessageReference(BaseModel):
    document_id: str
    document_name: str
    chunk_id: int
    pages: str
    score: float


class ChatSessionCount(BaseModel):
    chat_session_count: int


class ChatSessionForCollection(BaseModel):
    id: str
    latest_message_content: str | None
    updated_at: datetime


class ChatSessionInfo(BaseModel):
    id: str
    latest_message_content: str | None
    collection_id: str
    collection_name: str
    updated_at: datetime


class Chunk(BaseModel):
    text: str


class Chunks(BaseModel):
    result: list[Chunk]


class Collection(BaseModel):
    id: str
    name: str
    description: str
    document_count: int
    document_size: int
    created_at: datetime
    updated_at: datetime


class CollectionCount(BaseModel):
    collection_count: int


class CollectionInfo(BaseModel):
    id: str
    name: str
    description: str
    document_count: int
    document_size: int
    updated_at: datetime


class Document(BaseModel):
    id: str
    name: str
    type: str
    size: int
    page_count: int
    status: Status
    created_at: datetime
    updated_at: datetime

    class Config:
        use_enum_values = True


class DocumentCount(BaseModel):
    document_count: int


class DocumentInfo(BaseModel):
    id: str
    name: str
    type: str
    size: int
    page_count: int
    status: Status
    updated_at: datetime

    class Config:
        use_enum_values = True


class Identifier(BaseModel):
    id: str


class JobStatus(BaseModel):
    id: str
    status: str


class Job(BaseModel):
    id: str
    passed: float
    failed: float
    progress: float
    completed: bool
    canceled: bool
    date: datetime
    statuses: list[JobStatus]
    errors: list[str]


class Meta(BaseModel):
    version: str
    build: str
    username: str
    email: str
    license_expired: bool
    license_expiry_date: str


class ObjectCount(BaseModel):
    chat_session_count: int
    collection_count: int
    document_count: int


class Result(BaseModel):
    status: Status

    class Config:
        use_enum_values = True


class SchedulerStats(BaseModel):
    queue_length: int


class SearchResult(BaseModel):
    id: str
    topic: str
    name: str
    text: str
    size: int
    pages: str
    score: float


class SearchResults(BaseModel):
    result: list[SearchResult]


class SessionError(Exception):
    pass


@dataclass
class ChatRequest:
    t: Literal["cq"]
    mode: Literal["l", "s", "h"]  # l=lexical, s=semantic, h=hybrid
    session_id: str
    correlation_id: str
    body: str
    system_prompt: str | None
    pre_prompt_query: str | None
    prompt_query: str | None
    pre_prompt_summary: str | None
    prompt_summary: str | None
    llm: str | int | None
    llm_args: str | None


@dataclass
class ChatAcknowledgement:
    t: Literal["cx"]
    session_id: str
    correlation_id: str
    message_id: str


@dataclass
class ChatResponse:
    t: Literal["ca", "cp"]
    session_id: str
    message_id: str
    reply_to_id: str
    body: str


@dataclass
class ChatError:
    t: Literal["ce"]
    session_id: str
    reply_to_id: str
    body: str


class ObjectNotFoundError(Exception):
    pass


class InvalidArgumentError(Exception):
    pass

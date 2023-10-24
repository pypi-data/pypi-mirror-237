from logging import Logger
from typing import Any, Optional

from botocore.compat import ensure_bytes as ensure_bytes
from botocore.compat import ensure_unicode as ensure_unicode
from botocore.compat import urlparse as urlparse
from botocore.hooks import BaseEventHooks
from botocore.retryhandler import EXCEPTION_MAP as RETRYABLE_EXCEPTIONS

logger: Logger = ...

class Monitor:
    def __init__(self, adapter: Any, publisher: Any) -> None: ...
    def register(self, event_emitter: BaseEventHooks) -> None: ...
    def capture(self, event_name: str, **payload: Any) -> None: ...

class MonitorEventAdapter:
    def __init__(self, time: Any = ...) -> None: ...
    def feed(self, emitter_event_name: str, emitter_payload: Any) -> Any: ...

class BaseMonitorEvent:
    service: Any = ...
    operation: Any = ...
    timestamp: Any = ...
    def __init__(self, service: Any, operation: Any, timestamp: Any) -> None: ...
    def __eq__(self, other: Any) -> Any: ...

class APICallEvent(BaseMonitorEvent):
    latency: Any = ...
    attempts: int = ...
    retries_exceeded: Any = ...
    def __init__(
        self,
        service: Any,
        operation: Any,
        timestamp: Any,
        latency: Optional[Any] = ...,
        attempts: Optional[Any] = ...,
        retries_exceeded: bool = ...,
    ) -> None: ...
    def new_api_call_attempt(self, timestamp: Any) -> Any: ...

class APICallAttemptEvent(BaseMonitorEvent):
    latency: Any = ...
    url: Any = ...
    http_status_code: Any = ...
    request_headers: Any = ...
    response_headers: Any = ...
    parsed_error: Any = ...
    wire_exception: Any = ...
    def __init__(
        self,
        service: Any,
        operation: Any,
        timestamp: Any,
        latency: Optional[Any] = ...,
        url: Optional[Any] = ...,
        http_status_code: Optional[Any] = ...,
        request_headers: Optional[Any] = ...,
        response_headers: Optional[Any] = ...,
        parsed_error: Optional[Any] = ...,
        wire_exception: Optional[Any] = ...,
    ) -> None: ...

class CSMSerializer:
    csm_client_id: Any = ...
    def __init__(self, csm_client_id: Any) -> None: ...
    def serialize(self, event: Any) -> Any: ...

class SocketPublisher:
    def __init__(self, socket: Any, host: Any, port: Any, serializer: Any) -> None: ...
    def publish(self, event: Any) -> None: ...

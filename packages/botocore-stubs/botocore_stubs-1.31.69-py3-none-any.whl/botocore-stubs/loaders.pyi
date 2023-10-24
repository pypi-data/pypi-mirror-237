from logging import Logger
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Tuple, Type

from botocore import BOTOCORE_ROOT as BOTOCORE_ROOT
from botocore.compat import OrderedDict as OrderedDict
from botocore.exceptions import DataNotFoundError as DataNotFoundError
from botocore.exceptions import UnknownServiceError as UnknownServiceError
from botocore.utils import deep_merge as deep_merge

logger: Logger = ...

HAS_GZIP: bool

def instance_cache(func: Callable[..., Any]) -> Callable[..., Any]: ...

class JSONFileLoader:
    def exists(self, file_path: str) -> bool: ...
    def load_file(self, file_path: str) -> Any: ...

def create_loader(search_path_string: Optional[str] = ...) -> "Loader": ...

class Loader:
    FILE_LOADER_CLASS: Type[JSONFileLoader] = ...
    BUILTIN_DATA_PATH: str = ...
    CUSTOMER_DATA_PATH: str = ...
    BUILTIN_EXTRAS_TYPES: List[str] = ...
    def __init__(
        self,
        extra_search_paths: Optional[Iterable[str]] = ...,
        file_loader: Optional[JSONFileLoader] = ...,
        cache: Optional[Any] = ...,
        include_default_search_paths: bool = ...,
        include_default_extras: bool = ...,
    ) -> None:
        self.file_loader: JSONFileLoader
    @property
    def search_paths(self) -> List[str]: ...
    @property
    def extras_types(self) -> List[str]: ...
    def list_available_services(self, type_name: str) -> List[str]: ...
    def determine_latest_version(self, service_name: str, type_name: str) -> str: ...
    def list_api_versions(self, service_name: str, type_name: str) -> List[str]: ...
    def load_data_with_path(self, name: str) -> Tuple[Dict[str, Any], str]: ...
    def load_service_model(
        self, service_name: str, type_name: str, api_version: Optional[Any] = ...
    ) -> Any: ...
    def load_data(self, name: str) -> Any: ...
    def is_builtin_path(self, path: str) -> bool: ...

class ExtrasProcessor:
    def process(
        self, original_model: Mapping[str, Any], extra_models: Iterable[Mapping[str, Any]]
    ) -> None: ...

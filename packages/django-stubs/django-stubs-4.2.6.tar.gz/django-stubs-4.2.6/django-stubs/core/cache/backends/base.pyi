from collections.abc import Callable, Iterable, Iterator
from typing import Any

from django.core.exceptions import ImproperlyConfigured

class InvalidCacheBackendError(ImproperlyConfigured): ...
class CacheKeyWarning(RuntimeWarning): ...
class InvalidCacheKey(ValueError): ...

DEFAULT_TIMEOUT: Any
MEMCACHE_MAX_KEY_LENGTH: int

def default_key_func(key: Any, key_prefix: str, version: Any) -> str: ...
def get_key_func(key_func: Callable | str | None) -> Callable: ...

class BaseCache:
    _missing_key: object
    default_timeout: float | None
    _max_entries: int
    _cull_frequency: int
    key_prefix: str
    version: int
    key_func: Callable
    def __init__(self, params: dict[str, Any]) -> None: ...
    def get_backend_timeout(self, timeout: float | None = ...) -> float | None: ...
    def make_key(self, key: Any, version: int | None = ...) -> str: ...
    def validate_key(self, key: Any) -> None: ...
    def make_and_validate_key(self, key: Any, version: int | None = ...) -> str: ...
    def add(self, key: Any, value: Any, timeout: float | None = ..., version: int | None = ...) -> bool: ...
    async def aadd(self, key: Any, value: Any, timeout: float | None = ..., version: int | None = ...) -> bool: ...
    def get(self, key: Any, default: Any | None = ..., version: int | None = ...) -> Any: ...
    async def aget(self, key: Any, default: Any | None = ..., version: int | None = ...) -> Any: ...
    def set(self, key: Any, value: Any, timeout: float | None = ..., version: int | None = ...) -> None: ...
    async def aset(self, key: Any, value: Any, timeout: float | None = ..., version: int | None = ...) -> None: ...
    def touch(self, key: Any, timeout: float | None = ..., version: int | None = ...) -> bool: ...
    async def atouch(self, key: Any, timeout: float | None = ..., version: int | None = ...) -> bool: ...
    def delete(self, key: Any, version: int | None = ...) -> bool: ...
    async def adelete(self, key: Any, version: int | None = ...) -> bool: ...
    def get_many(self, keys: Iterable[Any], version: int | None = ...) -> dict[Any, Any]: ...
    async def aget_many(self, keys: Iterable[Any], version: int | None = ...) -> dict[Any, Any]: ...
    def get_or_set(
        self, key: Any, default: Any | None, timeout: float | None = ..., version: int | None = ...
    ) -> Any | None: ...
    async def aget_or_set(
        self, key: Any, default: Any | None, timeout: float | None = ..., version: int | None = ...
    ) -> Any | None: ...
    def has_key(self, key: Any, version: int | None = ...) -> bool: ...
    async def ahas_key(self, key: Any, version: int | None = ...) -> bool: ...
    def incr(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    async def aincr(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    def decr(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    async def adecr(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    def __contains__(self, key: Any) -> bool: ...
    def set_many(self, data: dict[Any, Any], timeout: float | None = ..., version: int | None = ...) -> list[Any]: ...
    async def aset_many(
        self, data: dict[Any, Any], timeout: float | None = ..., version: int | None = ...
    ) -> list[Any]: ...
    def delete_many(self, keys: Iterable[Any], version: int | None = ...) -> None: ...
    async def adelete_many(self, keys: Iterable[Any], version: int | None = ...) -> None: ...
    def clear(self) -> None: ...
    async def aclear(self) -> None: ...
    def incr_version(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    async def aincr_version(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    def decr_version(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    async def adecr_version(self, key: Any, delta: int = ..., version: int | None = ...) -> int: ...
    def close(self, **kwargs: Any) -> None: ...
    async def aclose(self, **kwargs: Any) -> None: ...

def memcache_key_warnings(key: str) -> Iterator[str]: ...

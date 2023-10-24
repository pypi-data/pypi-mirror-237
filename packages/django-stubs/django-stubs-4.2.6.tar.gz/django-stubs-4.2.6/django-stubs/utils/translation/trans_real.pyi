import gettext as gettext_module
from collections.abc import Iterator
from gettext import NullTranslations
from re import Pattern

# switch to tuple once https://github.com/python/mypy/issues/11098 is fixed
from typing import Any, Literal, Protocol, TypeVar

from django.http.request import HttpRequest
from typing_extensions import TypeAlias

CONTEXT_SEPARATOR: Literal["\x04"]
ACCEPT_LANGUAGE_HEADER_MAX_LENGTH: int

accept_language_re: Pattern[str]
language_code_re: Pattern[str]
language_code_prefix_re: Pattern[str]

class _PluralCallable(Protocol):
    def __call__(self, __n: int) -> int: ...

def reset_cache(*, setting: str, **kwargs: Any) -> None: ...

# switch to tuple once https://github.com/python/mypy/issues/11098 is fixed
_KeyT: TypeAlias = str | tuple[str, int]

_Z = TypeVar("_Z")

class TranslationCatalog:
    _catalogs: list[dict[_KeyT, str]]
    def __init__(self, trans: gettext_module.NullTranslations | None = ...) -> None: ...
    def __getitem__(self, key: _KeyT) -> str: ...
    def __setitem__(self, key: _KeyT, value: str) -> None: ...
    def __contains__(self, key: _KeyT) -> bool: ...
    def items(self) -> Iterator[tuple[_KeyT, str]]: ...
    def keys(self) -> Iterator[_KeyT]: ...
    def update(self, trans: gettext_module.NullTranslations) -> None: ...
    def get(self, key: _KeyT, default: _Z = ...) -> str | _Z: ...
    def plural(self, msgid: str, num: int) -> str: ...

class DjangoTranslation(gettext_module.GNUTranslations):
    domain: str
    plural: _PluralCallable
    def __init__(self, language: str, domain: str | None = ..., localedirs: list[str] | None = ...) -> None: ...
    def merge(self, other: NullTranslations) -> None: ...
    def language(self) -> str: ...
    def to_language(self) -> str: ...
    def ngettext(self, msgid1: str, msgid2: str, n: int) -> str: ...

def translation(language: str) -> DjangoTranslation: ...
def activate(language: str) -> None: ...
def deactivate() -> None: ...
def deactivate_all() -> None: ...
def get_language() -> str: ...
def get_language_bidi() -> bool: ...
def catalog() -> DjangoTranslation: ...
def gettext(message: str) -> str: ...
def pgettext(context: str, message: str) -> str: ...
def gettext_noop(message: str) -> str: ...
def do_ntranslate(singular: str, plural: str, number: float, translation_function: str) -> str: ...
def ngettext(singular: str, plural: str, number: float) -> str: ...
def npgettext(context: str, singular: str, plural: str, number: int) -> str: ...
def all_locale_paths() -> list[str]: ...
def check_for_language(lang_code: str | None) -> bool: ...
def get_languages() -> dict[str, str]: ...
def get_supported_language_variant(lang_code: str | None, strict: bool = ...) -> str: ...
def get_language_from_path(path: str, strict: bool = ...) -> str | None: ...
def get_language_from_request(request: HttpRequest, check_path: bool = ...) -> str: ...
def parse_accept_lang_header(lang_string: str) -> tuple[tuple[str, float], ...]: ...

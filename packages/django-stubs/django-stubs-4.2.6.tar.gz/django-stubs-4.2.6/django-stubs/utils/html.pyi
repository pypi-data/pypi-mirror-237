from collections.abc import Iterable
from html.parser import HTMLParser
from json import JSONEncoder
from re import Pattern
from typing import Any

from _typeshed import Incomplete
from django.utils.functional import SimpleLazyObject, _StrOrPromise
from django.utils.safestring import SafeData, SafeString

def escape(text: Any) -> SafeString: ...
def escapejs(value: Any) -> SafeString: ...
def json_script(value: Any, element_id: str | None = ..., encoder: type[JSONEncoder] | None = ...) -> SafeString: ...

# conditional_escape could use a protocol to be more precise, see https://github.com/typeddjango/django-stubs/issues/1474
def conditional_escape(text: _StrOrPromise | SafeData) -> SafeString: ...
def format_html(format_string: str, *args: Any, **kwargs: Any) -> SafeString: ...
def format_html_join(sep: str, format_string: str, args_generator: Iterable[Iterable[Any]]) -> SafeString: ...
def linebreaks(value: Any, autoescape: bool = ...) -> str: ...

class MLStripper(HTMLParser):
    fed: Any
    def __init__(self) -> None: ...
    def handle_data(self, d: str) -> None: ...
    def handle_entityref(self, name: str) -> None: ...
    def handle_charref(self, name: str) -> None: ...
    def get_data(self) -> str: ...

def strip_tags(value: str) -> str: ...
def strip_spaces_between_tags(value: str) -> str: ...
def smart_urlquote(url: str) -> str: ...
def urlize(text: str, trim_url_limit: int | None = ..., nofollow: bool = ..., autoescape: bool = ...) -> str: ...
def avoid_wrapping(value: str) -> str: ...
def html_safe(klass: type) -> type: ...

class Urlizer:
    trailing_punctuation_chars: str
    wrapping_punctuation: Incomplete
    word_split_re: Pattern[str] | SimpleLazyObject
    simple_url_re: Pattern[str] | SimpleLazyObject
    simple_url_2_re: Pattern[str] | SimpleLazyObject
    mailto_template: str
    url_template: str
    def __call__(
        self, text: Incomplete, trim_url_limit: Incomplete | None = ..., nofollow: bool = ..., autoescape: bool = ...
    ) -> Incomplete: ...
    def handle_word(
        self,
        word: Incomplete,
        *,
        safe_input: Incomplete,
        trim_url_limit: Incomplete | None = ...,
        nofollow: bool = ...,
        autoescape: bool = ...,
    ) -> Incomplete: ...
    def trim_url(self, x: str, *, limit: int | None) -> Incomplete: ...
    def trim_punctuation(self, word: str) -> tuple[str, str, str]: ...
    @staticmethod
    def is_email_simple(value: str) -> bool: ...

urlizer: Urlizer

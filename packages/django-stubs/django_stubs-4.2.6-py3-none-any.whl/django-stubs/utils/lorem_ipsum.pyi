from typing import Any

COMMON_P: str
WORDS: Any
COMMON_WORDS: Any

def sentence() -> str: ...
def paragraph() -> str: ...
def paragraphs(count: int, common: bool = ...) -> list[str]: ...
def words(count: int, common: bool = ...) -> str: ...

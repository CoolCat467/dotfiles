from collections.abc import Iterable
from idlelib.editor import EditorWindow as EditorWindow
from idlelib.filelist import FileList
from re import Pattern
from tkinter import Event, Misc
from typing import Any

file_line_pats: list[str]
file_line_progs: list[Pattern[str]] | None

def compile_progs() -> None: ...
def file_line_helper(line: str) -> tuple[str, int] | None: ...

class OutputWindow(EditorWindow):
    rmenu_specs: list[tuple[str | None, str | None, str | None]]
    allow_code_context: bool
    def __init__(self, *args: FileList | Misc | str | None) -> None: ...
    def ispythonsource(self, filename: str) -> bool: ...
    def short_title(self) -> str: ...
    def maybesave(self) -> str: ...
    def write(
        self, s: str, tags: tuple[str, ...] = ..., mark: str = ...
    ) -> int: ...
    def writelines(self, lines: Iterable[str]) -> None: ...
    def flush(self) -> None: ...
    def showerror(self, *args: str, **kwargs: Any) -> None: ...  # type: ignore[override]
    def goto_file_line(self, event: Event[Any] | None = ...) -> None: ...

class OnDemandOutputWindow:
    tagdefs: dict[str, dict[str, str]]
    flist: FileList
    owin: OutputWindow | None
    def __init__(self, flist: FileList) -> None: ...
    def write(self, s: str, tags: tuple[str] | None, mark: str) -> None: ...
    def setup(self) -> None: ...

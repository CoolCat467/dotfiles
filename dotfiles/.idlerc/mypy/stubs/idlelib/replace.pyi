from idlelib import searchengine as searchengine
from idlelib.searchbase import SearchDialogBase as SearchDialogBase
from tkinter import Entry, Event, Misc, StringVar, Text
from typing import Any

def replace(text: Text, insert_tags: str | None = ...) -> None: ...

class ReplaceDialog(SearchDialogBase):
    title: str
    icon: str
    replvar: StringVar
    insert_tags: str | None
    def __init__(
        self, root: Misc, engine: searchengine.SearchEngine
    ) -> None: ...
    ok: bool
    def open(self, text: Text, insert_tags: str | None = ...) -> None: ...
    replent: Entry
    def create_entries(self) -> None: ...
    def create_command_buttons(self) -> None: ...
    def find_it(self, event: Event[Any] | None = ...) -> None: ...
    def replace_it(self, event: Event[Any] | None = ...) -> None: ...
    def default_command(self, event: Event[Any] | None = ...) -> None: ...
    def replace_all(self, event: Event[Any] | None = ...) -> None: ...
    def do_find(self, ok: bool = ...) -> bool: ...
    def do_replace(self) -> bool: ...
    def show_hit(self, first: str, last: str) -> None: ...
    def close(self, event: Event[Any] | None = ...) -> None: ...

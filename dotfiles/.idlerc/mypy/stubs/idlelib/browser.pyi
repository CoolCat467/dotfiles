from collections.abc import Callable
from idlelib import pyshell as pyshell
from idlelib.config import idleConf as idleConf
from idlelib.tree import (
    ScrolledCanvas as ScrolledCanvas,
    TreeItem as TreeItem,
    TreeNode as TreeNode,
)
from idlelib.util import py_extensions as py_extensions
from idlelib.window import ListedToplevel as ListedToplevel
from tkinter import Event, Tk
from typing import Any

file_open: Callable[
    [str, bool | None], pyshell.EditorWindow | None
]  # pyshell.flist.open
browseable_extension_blocklist: tuple[str]

def is_browseable_extension(path: str) -> bool: ...
def transform_children(
    child_dict: dict[str, dict[str, str]], modname: str | None = ...
) -> list[dict[str, str]]: ...

class ModuleBrowser:
    master: Tk
    path: str
    def __init__(
        self, master: Tk, path: str, *, _htest: bool = ..., _utest: bool = ...
    ) -> None: ...
    def close(self, event: Event[Any] | None = ...) -> None: ...
    top: ListedToplevel
    node: TreeNode
    def init(self) -> None: ...
    def settitle(self) -> None: ...
    def rootnode(self) -> ModuleBrowserTreeItem: ...

class ModuleBrowserTreeItem(TreeItem):
    file: str
    def __init__(self, file: str) -> None: ...
    def GetText(self) -> str: ...
    def GetIconName(self) -> str: ...
    def GetSubList(self) -> list[TreeItem]: ...
    def OnDoubleClick(self) -> None: ...
    def IsExpandable(self) -> bool: ...
    def listchildren(self) -> list[dict[str, str]]: ...

class ChildBrowserTreeItem(TreeItem):
    obj: dict[str, str]
    name: str
    isfunction: bool
    def __init__(self, obj: dict[str, str]) -> None: ...
    def GetText(self) -> str: ...
    def GetIconName(self) -> str: ...
    def IsExpandable(self) -> bool: ...
    def GetSubList(self) -> list[TreeItem]: ...
    def OnDoubleClick(self) -> None: ...
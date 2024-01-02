from collections.abc import Mapping
from configparser import ConfigParser
from tkinter import Widget
from typing import Any, TypeVar

class InvalidConfigType(Exception): ...
class InvalidConfigSet(Exception): ...
class InvalidTheme(Exception): ...

class IdleConfParser(ConfigParser):
    file: str
    def __init__(
        self, cfgFile: str, cfgDefaults: Mapping[str, str | None] | None = ...
    ) -> None: ...
    def Get(
        self,
        section: str,
        option: str,
        type: str | None = ...,
        default: Any | None = ...,
        raw: bool = ...,
    ) -> str | int | bool: ...
    def GetOptionList(self, section: str) -> list[str | int | bool]: ...
    def Load(self) -> None: ...

class IdleUserConfParser(IdleConfParser):
    def SetOption(self, section: str, option: str, value: str) -> bool: ...
    def RemoveOption(self, section: str, option: str) -> bool: ...
    def AddSection(self, section: str) -> None: ...
    def RemoveEmptySections(self) -> None: ...
    def IsEmpty(self) -> bool: ...
    def Save(self) -> None: ...

_T = TypeVar("_T")

class IdleConf:
    config_types: tuple[str, str, str, str]
    defaultCfg: dict[str, IdleConfParser]
    userCfg: dict[str, IdleUserConfParser]
    cfg: dict[str, IdleConfParser | IdleUserConfParser]  # Unused currently
    def __init__(self, _utest: bool = ...) -> None: ...
    userdir: str
    def CreateConfigHandlers(self) -> None: ...
    def GetUserCfgDir(self) -> str: ...
    def GetOption(
        self,
        configType: str,
        section: str,
        option: str,
        default: _T | None = ...,
        type: str | None = ...,
        warn_on_default: bool = ...,
        raw: bool = ...,
    ) -> str | int | bool | _T | None: ...
    def SetOption(
        self,
        configType: str,
        section: str,
        option: str,
        value: str | int | bool,
    ) -> None: ...
    def GetSectionList(self, configSet: str, configType: str) -> list[str]: ...
    def GetHighlight(self, theme: str, element: str) -> dict[str, str]: ...
    def GetThemeDict(self, type: str, themeName: str) -> dict[str, str]: ...
    def CurrentTheme(self) -> str: ...
    def CurrentKeys(self) -> str: ...
    def current_colors_and_keys(self, section: str) -> str: ...
    @staticmethod
    def default_keys() -> str: ...
    def GetExtensions(
        self,
        active_only: bool = ...,
        editor_only: bool = ...,
        shell_only: bool = ...,
    ) -> list[str]: ...
    def RemoveKeyBindNames(self, extnNameList: list[str]) -> list[str]: ...
    def GetExtnNameForEvent(self, virtualEvent: str) -> str: ...
    def GetExtensionKeys(self, extensionName: str) -> dict[str, list[str]]: ...
    def GetExtensionBindings(
        self, extensionName: str
    ) -> dict[str, list[str]]: ...
    def GetKeyBinding(self, keySetName: str, eventStr: str) -> list[str]: ...
    def GetCurrentKeySet(self) -> dict[str, list[str]]: ...
    def GetKeySet(self, keySetName: str) -> dict[str, list[str]]: ...
    def IsCoreBinding(self, virtualEvent: str) -> bool: ...
    former_extension_events: set[str]
    def GetCoreKeys(
        self, keySetName: str | None = ...
    ) -> dict[str, list[str]]: ...
    def GetExtraHelpSourceList(
        self, configSet: str
    ) -> list[tuple[str, str, str]]: ...
    def GetAllExtraHelpSourcesList(self) -> list[tuple[str, str, str]]: ...
    def GetFont(
        self, root: Widget, configType: str, section: str
    ) -> tuple[str, int, str]: ...
    def LoadCfgFiles(self) -> None: ...
    def SaveUserCfgFiles(self) -> None: ...

idleConf: IdleConf

class ConfigChanges(dict[str, str | int | bool]):
    pages: list[str]
    def __init__(self) -> None: ...
    def add_option(
        self,
        config_type: str,
        section: str,
        item: str,
        value: int | bool | str,
    ) -> None: ...
    @staticmethod
    def save_option(
        config_type: str, section: str, item: str, value: int | bool | str
    ) -> bool: ...
    def save_all(self) -> bool: ...
    def delete_section(self, config_type: str, section: str) -> None: ...
    def clear(self) -> None: ...
from tkinter import BaseWidget, Widget

class TooltipBase:
    anchor_widget: Widget
    tipwindow: BaseWidget | None
    def __init__(self, anchor_widget: Widget) -> None: ...
    def __del__(self) -> None: ...
    def showtip(self) -> None: ...
    def position_window(self) -> None: ...
    def get_position(self) -> tuple[int, int]: ...
    def showcontents(self) -> None: ...
    def hidetip(self) -> None: ...

class OnHoverTooltipBase(TooltipBase):
    hover_delay: int
    def __init__(
        self, anchor_widget: Widget, hover_delay: int = ...
    ) -> None: ...
    def __del__(self) -> None: ...
    def schedule(self) -> None: ...
    def unschedule(self) -> None: ...
    def hidetip(self) -> None: ...

class Hovertip(OnHoverTooltipBase):
    text: str
    def __init__(
        self, anchor_widget: Widget, text: str, hover_delay: int = ...
    ) -> None: ...
    def showcontents(self) -> None: ...
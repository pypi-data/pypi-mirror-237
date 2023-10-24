"""Stub file for upload.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, List, Optional, Union, overload
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

files_state: str
upload_file: BaseVar
selected_files: BaseVar
clear_selected_files: BaseVar

class Upload(Component):
    @overload
    @classmethod
    def create(cls, *children, accept: Optional[Union[Var[Optional[Dict[str, List]]], Optional[Dict[str, List]]]] = None, disabled: Optional[Union[Var[bool], bool]] = None, max_files: Optional[Union[Var[int], int]] = None, max_size: Optional[Union[Var[int], int]] = None, min_size: Optional[Union[Var[int], int]] = None, multiple: Optional[Union[Var[bool], bool]] = None, no_click: Optional[Union[Var[bool], bool]] = None, no_drag: Optional[Union[Var[bool], bool]] = None, no_keyboard: Optional[Union[Var[bool], bool]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_drop: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Upload":  # type: ignore
        """Create an upload component.

               Args:
                   *children: The children of the component.
                   accept: The list of accepted file types. This should be a dictionary of MIME types as keys and array of file formats as
        values.
        supported MIME types: https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
                   disabled: Whether the dropzone is disabled.
                   max_files: The maximum number of files that can be uploaded.
                   max_size: The maximum file size (bytes) that can be uploaded.
                   min_size: The minimum file size (bytes) that can be uploaded.
                   multiple: Whether to allow multiple files to be uploaded.
                   no_click: Whether to disable click to upload.
                   no_drag: Whether to disable drag and drop.
                   no_keyboard: Whether to disable using the space/enter keys to upload.
                   **props: The properties of the component.

               Returns:
                   The upload component.
        """
        ...

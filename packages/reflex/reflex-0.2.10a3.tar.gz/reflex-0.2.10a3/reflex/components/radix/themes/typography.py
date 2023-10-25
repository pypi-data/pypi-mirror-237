"""Components for rendering text.

https://www.radix-ui.com/themes/docs/theme/typography
"""
from __future__ import annotations

from reflex.vars import Var

from .base import CommonMarginProps, RadixThemesComponent


class Text(CommonMarginProps, RadixThemesComponent):
    """A foundational text primitive based on the <span> element."""

    tag = "Text"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: Var[bool]

    # Change the default rendered element into a semantically appropriate alternative (cannot be used with asChild)
    as_: Var[str]

    # Text size: "1" - "9"
    size: Var[str]

    # Thickness of text: "light" | "regular" | "medium" | "bold"
    weight: Var[str]

    # Alignment of text in element: "left" | "center" | "right"
    align: Var[str]

    # Removes the leading trim space: "normal" | "start" | "end" | "both"
    trim: Var[str]

    # Overrides the accent color inherited from the Theme.
    color: Var[str]

    # Whether to render the text with higher contrast color
    high_contrast: Var[bool]


class Heading(Text):
    """A semantic heading element."""

    tag = "Heading"


class Blockquote(CommonMarginProps, RadixThemesComponent):
    """A block level extended quotation."""

    tag = "Blockquote"

    # Text size: "1" - "9"
    size: Var[str]

    # Thickness of text: "light" | "regular" | "medium" | "bold"
    weight: Var[str]

    # Overrides the accent color inherited from the Theme.
    color: Var[str]

    # Whether to render the text with higher contrast color
    high_contrast: Var[bool]


class Code(Blockquote):
    """Marks text to signify a short fragment of computer code."""

    tag = "Code"

    # The visual variant to apply: "solid" | "soft" | "outline" | "ghost"
    variant: Var[str]


class Em(CommonMarginProps, RadixThemesComponent):
    """Marks text to stress emphasis."""

    tag = "Em"


class Kbd(CommonMarginProps, RadixThemesComponent):
    """Represents keyboard input or a hotkey."""

    tag = "Kbd"

    # Text size: "1" - "9"
    size: Var[str]


class Link(CommonMarginProps, RadixThemesComponent):
    """A semantic element for navigation between pages."""

    tag = "Link"

    # Change the default rendered element for the one passed as a child, merging their props and behavior.
    as_child: Var[bool]

    # Text size: "1" - "9"
    size: Var[str]

    # Thickness of text: "light" | "regular" | "medium" | "bold"
    weight: Var[str]

    # Removes the leading trim space: "normal" | "start" | "end" | "both"
    trim: Var[str]

    # Sets the visibility of the underline affordance: "auto" | "hover" | "always"
    underline: Var[str]

    # Overrides the accent color inherited from the Theme.
    color: Var[str]

    # Whether to render the text with higher contrast color
    high_contrast: Var[bool]


class Quote(CommonMarginProps, RadixThemesComponent):
    """A short inline quotation."""

    tag = "Quote"


class Strong(CommonMarginProps, RadixThemesComponent):
    """Marks text to signify strong importance."""

    tag = "Strong"

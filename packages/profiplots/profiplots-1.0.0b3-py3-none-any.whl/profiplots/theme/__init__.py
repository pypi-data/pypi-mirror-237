"""
Package contains implementation of various themes (for example `default`). It also contains their specific implementations mapped to theme names, such as `GREYSCALE_CYCLER`.
"""

from cycler import cycler as _cycler

from profiplots import settings as _settings

__all__ = ["GREYSCALE_CYCLER", "COLOR_CYCLER"]

GREYSCALE_CYCLER = {"default": _cycler(color=["#7D7D7D", "#696969", "#555555", "#3C3C3C", "#282828"])}
"""Mapping of name of the theme to the color cycler of the theme with greyscale colors."""

COLOR_CYCLER = {"default": _cycler(color=["#465A9B", "#E63C41", "#B5578D", "#FFD21E", "#F3943B", "#41C34B", "#3DADE5"])}
"""Mapping of name of the theme to the color cycler of the theme with colors."""

assert all(k in _settings.SUPPORTED_THEMES for k in GREYSCALE_CYCLER), "Invalid theme name in `GREYSCALE_CYCLER`."
assert all(k in _settings.SUPPORTED_THEMES for k in COLOR_CYCLER), "Invalid theme name in `COLOR_CYCLER`."

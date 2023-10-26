"""
This package provides us with various styles. We can use them to modify the default theme look.
These styles include:

- `grey`: sets greyscale as the default color palette.
- `colored`: sets colored palette as the default.
- `grid`: adds grids to the plots.
- ...
"""

from profiplots.style._modifier import colored, grey, grid, spines, ticks

__all__ = [
    "grey",
    "colored",
    "grid",
    "spines",
    "ticks"
]

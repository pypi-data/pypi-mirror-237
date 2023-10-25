"""
This module contains colorschemes for all players on a pachisi board.
"""
import copy
from typing import Dict, List, Optional

from drawsvg.color import Hsl  # type: ignore

from pachisi_render.renderer.board import SVGColor

# fmt: off
_RED    = Hsl(  0 / 360, 1, 0.50)
_ORANGE = Hsl( 39 / 360, 1, 0.50)
_YELLOW = Hsl( 60 / 360, 1, 0.50)
_LIME   = Hsl(120 / 360, 1, 0.50)
_GREEN  = Hsl(120 / 360, 1, 0.25)
_AQUA   = Hsl(180 / 360, 1, 0.50)
_BLUE   = Hsl(240 / 360, 1, 0.50)
_PURPLE = Hsl(300 / 360, 1, 0.25)
# fmt: on


_BASE_COLORS: Dict[int, List[Hsl]] = {
    2: [_RED, _BLUE],
    3: [_RED, _GREEN, _BLUE],
    4: [_RED, _YELLOW, _GREEN, _BLUE],
    5: [_RED, _ORANGE, _YELLOW, _GREEN, _BLUE],
    6: [_RED, _ORANGE, _YELLOW, _GREEN, _BLUE, _PURPLE],
    7: [_RED, _ORANGE, _YELLOW, _LIME, _GREEN, _BLUE, _PURPLE],
    8: [_RED, _ORANGE, _YELLOW, _LIME, _GREEN, _AQUA, _BLUE, _PURPLE],
}


class PlayerColorscheme:
    """
    A player's colorscheme.
    """

    def __init__(self, base_color: Hsl):
        self._base_color = base_color

    @property
    def field_color(self) -> SVGColor:
        """
        Get the color of the player's fields.
        """
        color = copy.deepcopy(self._base_color)
        color.s *= 1
        color.l *= 1
        return str(color)

    @property
    def piece_color(self) -> SVGColor:
        """
        Get the color of the player's pieces.
        """
        color = copy.deepcopy(self._base_color)
        color.s *= 1
        color.l *= 1
        return str(color)

    @property
    def mark_color(self) -> SVGColor:
        """
        Get the color of the player's marks.
        """
        color = copy.deepcopy(self._base_color)
        color.s *= 1
        color.l *= 0.5
        return str(color)

    @property
    def background_color(self) -> SVGColor:
        """
        Get the color of the player's home's/goal's backgrounds.
        """
        color = copy.deepcopy(self._base_color)
        color.s *= 1
        color.l *= 0.5
        return str(color)


class Colorscheme:
    """
    A colorscheme for a pachisi board with some number of players.
    """

    def __init__(self, player_count: int = 2):
        base_colors = _BASE_COLORS[player_count]
        self._players = [PlayerColorscheme(base) for base in base_colors]

    def line_color(self) -> SVGColor:
        """
        Get the color of all lines on the board.
        """
        return "black"

    def field_color(self, player_id: Optional[int] = None) -> SVGColor:
        """
        Get the color of the given player's fields.
        """
        if player_id is not None:
            return self._players[player_id].field_color
        return "black"

    def piece_color(self, player_id: Optional[int] = None) -> SVGColor:
        """
        Get the color of the given player's pieces.
        """
        if player_id is not None:
            return self._players[player_id].piece_color
        return "lightgrey"

    def mark_color(self, player_id: Optional[int] = None) -> SVGColor:
        """
        Get the color of the given player's marks.
        """
        if player_id is not None:
            return self._players[player_id].mark_color
        return "black"

    def background_color(self, player_id: Optional[int] = None) -> SVGColor:
        """
        Get the color of the given player's home's/goal's backgrounds.
        """
        if player_id is not None:
            return self._players[player_id].background_color
        return "white"

"""
This module contains the Board class and its constituent parts.
"""

import dataclasses
from dataclasses import dataclass
from enum import IntEnum
from typing import Dict, List, Optional, Tuple

SVGColor = str
PlayerId = int


class Decoration(IntEnum):
    """
    Types of Decoration that may be used as FieldMarks.
    """

    CIRCLE = 0
    DOT = 1
    DASH = 2
    TRIANGLE = 3
    SQUARE = 4
    PLUS = 5
    CROSS = 6
    STAR = 7


@dataclass
class FieldMark:
    """
    Describes a mark that may be placed on the board's fields.
    """

    decoration: Decoration
    name: str = ""
    description: str = ""


@dataclass
class Field:
    """
    A field on a pachisi board.
    """

    field_color: SVGColor = "black"
    piece_color: SVGColor = "grey"
    mark_color: SVGColor = "black"
    mark: Optional[FieldMark] = None
    text: Optional[str] = None


@dataclass
class Group:
    """
    A group of fields on a pachisi board.
    """

    fields: List[Field]
    background_color: SVGColor = "lightgrey"
    ordered: bool = False

    def __len__(self) -> int:
        return len(self.fields)


@dataclass
class Board:
    """
    A representation of a pachisi board.
    """

    homes: Dict[int, Group]
    loop: List[Field]
    goals: Dict[int, Group]
    shortcuts: List[Tuple[int, int]] = dataclasses.field(default_factory=lambda: [])
    marks: List[FieldMark] = dataclasses.field(default_factory=lambda: [])

    def __post_init__(self):  # pylint: disable=too-many-branches
        if len(self.homes) != len(self.goals):
            raise ValueError("There must be an equal number of homes and goals!")
        for idx in self.homes:
            if idx < 0 or len(self.loop) < idx:
                raise ValueError(
                    f"Home cannot be connected to {idx}, this index does not exist in loop"
                )
        for idx in self.goals:
            if idx < 0 or len(self.loop) < idx:
                raise ValueError(
                    f"Goal cannot be connected to {idx}, this index does not exist in loop"
                )
        for idx1, idx2 in self.shortcuts:
            if idx1 < 0 or len(self.loop) <= idx1:
                raise ValueError(
                    f"Shortcut cannot start at {idx1}, this index does not exist in loop"
                )
            if idx2 < 0 or len(self.loop) <= idx2:
                raise ValueError(
                    f"Shortcut cannot end at {idx2}, this index does not exist in loop"
                )
        for home in self.homes.values():
            for field in home.fields:
                if field.mark and field.mark not in self.marks:
                    raise ValueError("Field's mark does not appear in board's marks")
        for field in self.loop:
            if field.mark and field.mark not in self.marks:
                raise ValueError("Field's mark does not appear in board's marks")
        for goal in self.goals.values():
            for field in goal.fields:
                if field.mark and field.mark not in self.marks:
                    raise ValueError("Field's mark does not appear in board's marks")

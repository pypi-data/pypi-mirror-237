"""
This module contains classes to easily represent a simple pachisi board.
"""
from typing import List, Optional, Tuple

import pydantic as pd
from pydantic.dataclasses import dataclass

from pachisi_render.renderer.board import Decoration

D_LOOP = 40


PlayerId = int
MarkId = int
LoopIndex = int


@dataclass
class MarkType:
    """
    A mark which can be placed on fields.
    """

    id: MarkId = pd.Field(description="The mark's id. Can be referred to when placing marks.")
    decoration: Decoration = pd.Field(
        description="A symbol to be displayed when the mark is placed."
    )
    name: str = pd.Field(
        "", description="A name for the mark. Should correspond to the mark's meaning."
    )
    description: str = pd.Field("", description="A description for the mark.")


@dataclass
class MarkPlacement:
    """
    A mark placed on a field or piece.
    """

    kind: MarkId = pd.Field(
        description=(
            "The id of the type of mark to be displayed here. Types of marks are defined at the"
            " BoardState level and the id given here must correspond to the id of a mark defined"
            " there."
        )
    )
    owner: Optional[PlayerId] = pd.Field(
        None, ge=0, le=7, description="The player whom this mark belongs to."
    )


@dataclass
class FieldState:
    """
    Fields are all the positions in which pieces can be placed on the
    board. Fields can be empty or be occupied by some player's piece(s).
    """

    occupant: Optional[PlayerId] = pd.Field(
        None, description="The piece currently occupying this field."
    )
    mark: Optional[MarkPlacement] = pd.Field(
        None, description="A mark to be placed on this field."
    )
    text: Optional[str] = pd.Field(
        None,
        description=(
            "Text to be displayed on this field. For optimal visual results, use no more than 4"
            " characters."
        ),
    )

    @property  # pylint: disable-next=missing-function-docstring
    def occupied(self) -> bool:
        return self.occupant is not None

    @property  # pylint: disable-next=missing-function-docstring
    def marked(self) -> bool:
        return self.mark is not None


@dataclass
class HomeState:
    """
    The state of a player's home. This is where the player keeps pieces
    not yet introduced into the game.
    """

    owner: PlayerId = pd.Field(
        None, ge=0, le=7, description="The id of the player whom this home belongs to."
    )
    start: LoopIndex = pd.Field(
        0,
        description=(
            "The index of the field in the loop on which pieces departing from this home will"
            " start."
        ),
    )
    fields: List[FieldState] = pd.Field(
        default_factory=lambda: [], description="The list of fields this home consists of."
    )


@dataclass
class GoalState:
    """
    The state of a player's goal. This is where the player's pieces end
    up after completing their journey through the loop.
    """

    owner: PlayerId = pd.Field(
        None, ge=0, le=7, description="The id of the player whom this goal belongs to."
    )
    entrance: LoopIndex = pd.Field(
        0, description="The index of the field in the loop from which pieces can enter this goal."
    )
    fields: List[FieldState] = pd.Field(
        default_factory=lambda: [], description="The list of fields this goal consists of."
    )


@dataclass
class BoardState:
    """
    A simple representation of a pachisi board.

    The board consists of fields on which pieces can be placed. It can
    be broken up roughly into three parts: houses, the main loop and
    goals.

    Pieces start in a player's house, then enter the loop at the
    player's start field, traverse the loop and, at the goal's entrance,
    exit it into the player's goal.

    Please note: if any part of the board requires a player id, this id
    must be between 0 and (player_count - 1).
    """

    player_count: int = pd.Field(
        default=0, ge=0, le=8, description="Number of players on the board."
    )
    homes: List[HomeState] = pd.Field(
        default_factory=lambda: [], description="All player's homes in no specific order."
    )
    loop: List[FieldState] = pd.Field(
        default_factory=lambda: [], description="The board's main loop."
    )
    goals: List[GoalState] = pd.Field(
        default_factory=lambda: [], description="All player's goals in no specific order."
    )
    shortcuts: List[Tuple[int, int]] = pd.Field(
        default_factory=lambda: [],
        description=(
            "Directed edges between two fields in the main loop. Encoded as a list of tuples of"
            " loop indices."
        ),
    )
    goals_ordered: bool = pd.Field(
        default=True,
        description=(
            "Whether the goals on this board must be traversed in a specific order or not."
        ),
    )
    marks: List[MarkType] = pd.Field(
        default_factory=lambda: [], description="A map of MarkIds to FieldMarks."
    )

    @property  # pylint: disable-next=missing-function-docstring
    def _fields(self) -> List[FieldState]:
        """
        Returns all fields on the board.
        """
        return (
            [field for home in self.homes for field in home.fields]
            + list(self.loop)
            + [field for goal in self.goals for field in goal.fields]
        )

    @property  # pylint: disable-next=missing-function-docstring
    def _mark_placements(self) -> List[MarkPlacement]:
        """
        Returns all mark placements on the board.
        """
        return [field.mark for field in self._fields if field.mark]

    def mark_type(self, mark_id: MarkId) -> MarkType:
        """
        Get a mark type by its id.
        """
        return next(mark for mark in self.marks if mark.id == mark_id)

    def home_of(self, player_id: PlayerId) -> HomeState:
        """
        Returns the given player's home.
        """
        return next(home for home in self.homes if home.owner == player_id)

    def goal_of(self, player_id: PlayerId) -> GoalState:
        """
        Returns the given player's goal.
        """
        return next(goal for goal in self.goals if goal.owner == player_id)

    @pd.field_validator("homes", mode="after")
    @classmethod  # pylint: disable-next=missing-function-docstring
    def distinct_start(cls, value: List[HomeState]) -> List[HomeState]:
        starts: set[int] = set()
        for home in value:
            if home.start in starts:
                raise ValueError(
                    "All homes must have distinct start fields. "
                    f"In violation, field {home.start} is used by at least two homes."
                )
            starts.add(home.start)
        return value

    @pd.field_validator("goals", mode="after")
    @classmethod  # pylint: disable-next=missing-function-docstring
    def distinct_entrance(cls, value: List[GoalState]) -> List[GoalState]:
        entrances: set[int] = set()
        for goal in value:
            if goal.entrance in entrances:
                raise ValueError(
                    "All homes must have distinct start fields. "
                    f"In violation, field {goal.entrance} is used by at least two goals."
                )
            entrances.add(goal.entrance)
        return value

    @pd.model_validator(mode="after")  # pylint: disable-next=missing-function-docstring
    def shortcuts_in_loop(self) -> "BoardState":
        for i, j in self.shortcuts:
            if i not in range(len(self.loop)) or j not in range(len(self.loop)):
                raise ValueError(f"Shortcut {(i,j)} outside loop's bounds")
        return self

    @pd.model_validator(mode="after")  # pylint: disable-next=missing-function-docstring
    def marks_known(self) -> "BoardState":
        for mark in self._mark_placements:
            if mark.kind not in self.marks:
                raise ValueError(f"reference to unknown mark_id {mark.kind}")
        return self

    @pd.model_validator(mode="after")  # pylint: disable-next=missing-function-docstring
    def playerid_in_bounds(self) -> "BoardState":
        references = (
            [home.owner for home in self.homes]
            + [goal.owner for goal in self.goals]
            + [field.occupant for field in self._fields if field.occupant is not None]
            + [mark.owner for mark in self._mark_placements if mark.owner is not None]
        )
        for reference in references:
            if reference not in range(self.player_count):
                raise ValueError(
                    f"player_id {reference} is not valid on a board with "
                    f"{self.player_count} players."
                )
        return self

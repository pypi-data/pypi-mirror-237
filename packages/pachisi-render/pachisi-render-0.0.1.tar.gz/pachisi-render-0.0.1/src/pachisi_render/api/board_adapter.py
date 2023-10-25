"""
This module contains a functional class which can be used to transform
BoardStates into Boards.
"""
from typing import Dict, List, Optional, Tuple

from pachisi_render.api.colorscheme import Colorscheme
from pachisi_render.api.state import BoardState, FieldState
from pachisi_render.renderer.board import Board, Field, FieldMark, Group


class BoardAdapter:
    """
    Adapter between BoardState and Board instances.
    """

    def __init__(self, state: BoardState) -> None:
        self.state = state
        self.colorscheme = Colorscheme(state.player_count)

    def state_index(self, board_index) -> int:
        """
        For users of the api, it is presumably more convenient to let
        loop start and end at no specific field.
        But for rendering, results visually improve if we start the loop
        at the first player's goal entrance.
        This method takes an index in the rendering-friendly loop and
        returns the corresponding index in the api-friendly loop.
        """
        goal_0_offset = self.state.goal_of(0).entrance
        return (board_index + goal_0_offset) % len(self.state.loop)

    def board_index(self, state_index) -> int:
        """
        Inverse index transformation of state_index.
        """
        goal_0_offset = self.state.goal_of(0).entrance
        return (state_index - goal_0_offset) % len(self.state.loop)

    def _process_field(self, field_state: FieldState, owner: Optional[int] = None) -> Field:
        field_color = self.colorscheme.field_color(owner)
        piece_color = self.colorscheme.piece_color()
        mark_color = self.colorscheme.mark_color()
        mark = None

        if field_state.marked:
            assert field_state.mark is not None
            mark_color = self.colorscheme.mark_color(field_state.mark.owner)
            mark_type = self.state.marks[field_state.mark.kind]
            mark = FieldMark(mark_type.decoration, mark_type.name, mark_type.description)

        if field_state.occupied:
            assert field_state.occupant is not None
            piece_color = self.colorscheme.piece_color(field_state.occupant)

        return Field(field_color, piece_color, mark_color, mark, field_state.text)

    @property  # pylint: disable-next=missing-function-docstring
    def homes(self) -> Dict[int, Group]:
        homes: Dict[int, Group] = {}
        for home in self.state.homes:
            index = self.board_index(home.start)
            fields = [self._process_field(field_state, home.owner) for field_state in home.fields]
            background_color = self.colorscheme.background_color(home.owner)

            homes[index] = Group(fields, background_color)
        return homes

    @property  # pylint: disable-next=missing-function-docstring
    def loop(self) -> List[Field]:
        loop: List[Field] = []
        for i in range(len(self.state.loop)):
            state_index = self.state_index(i)
            field_state = self.state.loop[state_index]

            owner = None
            # is this field anyone's start field?
            for home in self.state.homes:
                if home.start == state_index:
                    owner = home.owner
                    break

            loop.append(self._process_field(field_state, owner))
        return loop

    @property  # pylint: disable-next=missing-function-docstring
    def goals(self) -> Dict[int, Group]:
        goals: Dict[int, Group] = {}
        for goal in self.state.goals:
            index = self.board_index(goal.entrance)
            fields = [self._process_field(field_state, goal.owner) for field_state in goal.fields]
            background_color = self.colorscheme.background_color(goal.owner)
            ordered = self.state.goals_ordered

            goals[index] = Group(fields, background_color, ordered)
        return goals

    @property  # pylint: disable-next=missing-function-docstring
    def shortcuts(self) -> List[Tuple[int, int]]:
        # We need to adapt the shortcuts to the moved indexes in the loop
        return [
            (self.board_index(start), self.board_index(end)) for start, end in self.state.shortcuts
        ]

    @property  # pylint: disable-next=missing-function-docstring
    def marks(self) -> List[FieldMark]:
        return [
            FieldMark(mark.decoration, mark.name, mark.description) for mark in self.state.marks
        ]

    def convert(self) -> Board:
        """
        Store as an actual Board instance.
        """
        return Board(self.homes, self.loop, self.goals, self.shortcuts, self.marks)

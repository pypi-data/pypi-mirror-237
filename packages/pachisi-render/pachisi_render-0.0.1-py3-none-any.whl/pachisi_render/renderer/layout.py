"""
This module contains a layouter for arranging the geometric primitives
that make up a pachisi board.
"""
from __future__ import annotations

import copy
import math
from abc import ABC, abstractmethod
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Tuple

import drawsvg as dw  # type: ignore

from pachisi_render.renderer.board import (
    Board,
    Decoration,
    Field,
    FieldMark,
    Group,
    SVGColor,
)

FIELD_INNER_RADIUS: float = 22.5
FIELD_BORDER: float = 5.0
FIELD_MARGIN: float = 7.5
FIELD_RADIUS: float = FIELD_INNER_RADIUS + FIELD_BORDER
BACKGROUND_RADIUS: float = FIELD_RADIUS + 5
LINE_WIDTH: float = 2.5
GRID: float = 2 * (FIELD_RADIUS + FIELD_MARGIN)
MARK_RADIUS: float = 2 / 3 * FIELD_INNER_RADIUS
MARK_STROKE_WIDTH: float = FIELD_BORDER
HOME_PADDING: float = GRID
FIELD_FONT_SIZE: float = 20
TEXT_FONT_SIZE: float = 30

# Available positions depend on player count (key)
COUNT_TO_POSITIONS: Dict[int, List[int]] = {
    1: [7],
    2: [1, 5],
    3: [0, 3, 5],
    4: [1, 3, 5, 7],
    5: [0, 2, 3, 5, 6],
    6: [1, 2, 3, 5, 6, 7],
    7: [0, 1, 2, 3, 5, 6, 7],
    8: [0, 1, 2, 3, 4, 5, 6, 7],
}

DEFAULT_LINE_COLOR: SVGColor = "black"

L_BACKGROUND: int = 1
L_LINES: int = 2
L_FIELDS: int = 3
L_MARKS: int = 4
L_TEXT: int = 5

EPSILON = 1e-3


class Layout(Enum):
    """
    This enum specifies all supported layouts for pachisi boards.
    """

    WHEEL = "wheel"
    SUN = "sun"


@dataclass(frozen=True)
class LayoutOpts:
    """
    Specify how a pachisi board should be rendered.
    """

    layout: Layout = Layout.WHEEL
    show_text: bool = False
    show_mark_explanation: bool = False


@dataclass
class Vec2:
    """
    Simple 2d vector.
    Supports addition, subtraction and scalar multiplication.
    """

    x: float = 0
    y: float = 0

    @classmethod
    def from_radial(cls, radius: float, angle: float):
        """
        Create a vector from radial coordinates (angle in radians).
        WARNING: Contrary to common definitions of polar coordinates, an
        angle of 0 is north and angles increase clockwise.
        """
        # We chose this somewhat strange definition of coordinates
        # because it makes most of our calculations easier.
        # This is in pard because we assume pachisi boards to use a
        # clockwise direction of play, and for creating a nice layout
        # it has proven useful to begin layouting in the north.
        return Vec2(x=radius * math.sin(angle), y=radius * math.cos(angle))

    @property
    def length(self) -> float:
        """
        The vector's euclidian magnitude.
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self) -> Vec2:
        """
        Returns a normalized version of this vector.
        """
        return Vec2(self.x / self.length, self.y / self.length)

    def __neg__(self) -> Vec2:
        return Vec2(-self.x, -self.y)

    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2) -> Vec2:
        return self + (-other)

    def __mul__(self, scale: int | float) -> Vec2:
        return Vec2(self.x * scale, self.y * scale)

    __rmul__ = __mul__


class BoundingBox:
    """
    A bounding box around 2d geometry.
    """

    def __init__(self, corner1: Vec2 = Vec2(), corner2: Vec2 = Vec2()) -> None:
        self.corner_bl = corner1
        self.corner_tr = corner1
        self.extend_to(corner2)

    @property  # pylint: disable-next=missing-function-docstring
    def width(self) -> float:
        return self.corner_tr.x - self.corner_bl.x

    @property  # pylint: disable-next=missing-function-docstring
    def height(self) -> float:
        return self.corner_tr.y - self.corner_bl.y

    @property  # pylint: disable-next=missing-function-docstring
    def center(self) -> Vec2:
        x = (self.corner_bl.x + self.corner_tr.x) / 2
        y = (self.corner_bl.y + self.corner_tr.y) / 2
        return Vec2(x, y)

    @property
    def corners(self) -> Tuple[Vec2, Vec2, Vec2, Vec2]:
        """
        All four corners of the bounding box, starting top-right and
        proceeding clockwise.
        """
        return (
            self.corner_tr,
            self.corner_bl + Vec2(self.width, 0),
            self.corner_bl,
            self.corner_bl + Vec2(0, self.height),
        )

    def canvas_radius(self) -> float:
        """
        The radius of the smallest possible circle centered in (0,0)
        that would encompass this box.
        """
        return max(corner.length for corner in self.corners)

    def extend_to(self, pos: Vec2) -> None:
        """
        Extend this bounding box until it encompasses the given
        position.
        """
        min_x = min(self.corner_bl.x, pos.x)
        min_y = min(self.corner_bl.y, pos.y)

        max_x = max(self.corner_tr.x, pos.x)
        max_y = max(self.corner_tr.y, pos.y)

        self.corner_bl = Vec2(min_x, min_y)
        self.corner_tr = Vec2(max_x, max_y)

    def extend_by(self, distance: float) -> None:
        """
        Enlarge this bounding box in all directions by the given
        distance.
        """
        self.corner_bl.x -= distance
        self.corner_bl.y -= distance
        self.corner_tr.x += distance
        self.corner_tr.y += distance

    def union(self, other: BoundingBox) -> BoundingBox:
        """
        Creates a bounding box encompassing both this bounding box and
        the given bounding box.
        """
        box = copy.deepcopy(self)
        box.extend_to(other.corner_bl)
        box.extend_to(other.corner_tr)
        return box


class LayeredCanvas:
    """
    A collection of drawing elements, ordered into layers. When drawn,
    contained elements are drawn in order from lowest to highest layer
    with resulting occlusion.
    """

    def __init__(self) -> None:
        self._layers: Dict[int, List[dw.DrawingElement]] = defaultdict(lambda: [])

    def add_to(self, layer: int, element: dw.types.DrawingElement) -> None:
        """
        Add the given element to the given layer.
        """
        self._layers[layer].append(element)

    def draw(self, drawing: dw.Drawing) -> None:
        """
        Draw all contained elements onto the given drawing.
        """
        for _, layer in sorted(self._layers.items()):
            for element in layer:
                drawing.append(element)


# pylint: disable-next=too-few-public-methods
class Element(ABC):
    """
    Some geometry.
    """

    @abstractmethod
    def canvas_radius(self, opts: LayoutOpts) -> float:
        """
        The radius of the smallest possible circle centered in (0,0)
        that would encompass this element.
        """
        raise NotImplementedError()

    @abstractmethod
    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        """
        Create a bounding box around the geometry in this element.
        """
        raise NotImplementedError()

    @abstractmethod
    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        """
        Draw this element onto the given canvas.
        """
        raise NotImplementedError()


@dataclass
class FieldElement(Element):
    """
    Geometry for a field on a pachisi board.
    """

    field: Field
    position: Vec2

    def canvas_radius(self, opts: LayoutOpts) -> float:
        return self.position.length + FIELD_RADIUS

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        box = BoundingBox(self.position, self.position)
        box.extend_by(FIELD_RADIUS)
        return box

    def _draw_dash(self, canvas: LayeredCanvas, angle: float = 0) -> None:
        """
        Helper function to draw the field's dash mark at the specified
        angle from horizontal.
        """
        canvas.add_to(
            L_MARKS,
            dw.Line(
                self.position.x - MARK_RADIUS,
                self.position.y,
                self.position.x + MARK_RADIUS,
                self.position.y,
                stroke_width=MARK_STROKE_WIDTH,
                stroke=self.field.mark_color,
                transform=f"rotate({angle:f}, {self.position.x}, {-self.position.y})",
            ),
        )

    def _draw_plus(self, canvas: LayeredCanvas, angle: float = 0) -> None:
        """
        Helper function to draw the field's plus mark at the specified
        angle.
        """
        self._draw_dash(canvas, 0 + angle)
        self._draw_dash(canvas, 90 + angle)

    def draw_mark(self, canvas: LayeredCanvas) -> None:
        """
        Draws just the field's mark
        """
        if not self.field.mark:
            return
        if self.field.mark.decoration == Decoration.CIRCLE:
            canvas.add_to(
                L_MARKS,
                dw.Circle(
                    self.position.x,
                    self.position.y,
                    r=MARK_RADIUS,
                    fill=self.field.mark_color,
                ),
            )
        elif self.field.mark.decoration == Decoration.DOT:
            canvas.add_to(
                L_MARKS,
                dw.Circle(
                    self.position.x,
                    self.position.y,
                    r=MARK_STROKE_WIDTH / 2,
                    fill=self.field.mark_color,
                    stroke_width=0,
                ),
            )
        elif self.field.mark.decoration == Decoration.DASH:
            self._draw_dash(canvas)
        elif self.field.mark.decoration == Decoration.TRIANGLE:
            points = (
                self.position + Vec2.from_radial(MARK_RADIUS, 0),
                self.position + Vec2.from_radial(MARK_RADIUS, 2 / 3 * math.pi),
                self.position + Vec2.from_radial(MARK_RADIUS, 4 / 3 * math.pi),
            )
            canvas.add_to(
                L_MARKS,
                dw.Lines(
                    points[0].x,
                    points[0].y,
                    points[1].x,
                    points[1].y,
                    points[2].x,
                    points[2].y,
                    close=True,
                    fill=self.field.mark_color,
                ),
            )
        elif self.field.mark.decoration == Decoration.SQUARE:
            canvas.add_to(
                L_MARKS,
                dw.Rectangle(
                    self.position.x - MARK_RADIUS / 2,
                    self.position.y - MARK_RADIUS / 2,
                    MARK_RADIUS,
                    MARK_RADIUS,
                    fill=self.field.mark_color,
                ),
            )
        elif self.field.mark.decoration == Decoration.PLUS:
            self._draw_plus(canvas)
        elif self.field.mark.decoration == Decoration.CROSS:
            self._draw_plus(canvas, 45)
        elif self.field.mark.decoration == Decoration.STAR:
            self._draw_plus(canvas, 0)
            self._draw_plus(canvas, 45)

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        canvas.add_to(
            L_FIELDS,
            dw.Circle(
                self.position.x,
                self.position.y,
                r=FIELD_INNER_RADIUS + FIELD_BORDER / 2,
                fill=self.field.piece_color,
                stroke_width=FIELD_BORDER,
                stroke=self.field.field_color,
            ),
        )
        if self.field.text and opts.show_text:
            canvas.add_to(
                L_TEXT,
                dw.Text(
                    self.field.text,
                    FIELD_FONT_SIZE,
                    self.position.x,
                    self.position.y,
                    text_anchor="middle",
                    dominant_baseline="central",
                ),
            )
        self.draw_mark(canvas)


@dataclass
class Line(Element):
    """
    A straight line between two points.
    """

    start: Vec2
    end: Vec2

    def canvas_radius(self, opts: LayoutOpts) -> float:
        return max(self.start.length, self.end.length) + LINE_WIDTH / 2

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        box = BoundingBox(self.start, self.end)
        box.extend_by(LINE_WIDTH / 2)
        return box

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        canvas.add_to(
            L_LINES,
            dw.Line(
                self.start.x,
                self.start.y,
                self.end.x,
                self.end.y,
                stroke=DEFAULT_LINE_COLOR,
                stroke_width=LINE_WIDTH,
            ),
        )


@dataclass
class ShortcutElement(Element):
    """
    A line representing a shortcut through the board's center
    connecting two fields.
    """

    start: Vec2
    end: Vec2

    def canvas_radius(self, opts: LayoutOpts) -> float:
        return max(self.start.length, self.end.length) + LINE_WIDTH

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        box = BoundingBox(self.start, self.end)
        box.extend_by(LINE_WIDTH)
        return box

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        path = dw.Path(
            stroke=DEFAULT_LINE_COLOR,
            stroke_width=LINE_WIDTH,
            stroke_dasharray=str(LINE_WIDTH),
            fill="none",
        )
        canvas.add_to(L_LINES, path.M(self.start.x, self.start.y).Q(0, 0, self.end.x, self.end.y))


@dataclass
class Circle(Element):
    """
    A circular line.
    """

    center: Vec2
    radius: float

    def canvas_radius(self, opts: LayoutOpts) -> float:
        return self.center.length + self.radius + LINE_WIDTH / 2

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        box = BoundingBox(self.center, self.center)
        box.extend_by(self.radius + LINE_WIDTH / 2)  # overestimation
        return box

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        canvas.add_to(
            L_LINES,
            dw.Circle(
                self.center.x,
                self.center.y,
                self.radius,
                stroke=DEFAULT_LINE_COLOR,
                stroke_width=LINE_WIDTH,
                fill="none",
            ),
        )


@dataclass
class BackgroundLine(Element):
    """
    A background for a line of fields.
    Start and end are just the coordinates of the outermost fields'
    centers.
    """

    start: Vec2
    end: Vec2
    color: SVGColor

    def canvas_radius(self, opts: LayoutOpts) -> float:
        return max(self.start.length, self.end.length) + BACKGROUND_RADIUS

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        box = BoundingBox(self.start, self.end)
        box.extend_by(BACKGROUND_RADIUS)
        return box

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        canvas.add_to(
            L_BACKGROUND,
            dw.Line(
                self.start.x,
                self.start.y,
                self.end.x,
                self.end.y,
                stroke=self.color,
                stroke_width=2 * BACKGROUND_RADIUS,
                stroke_linecap="round",
            ),
        )


@dataclass
class BackgroundRect(Element):
    """
    A rectangular, axis-aligned background for a set of fields.
    """

    corner_a: Vec2
    corner_b: Vec2
    color: SVGColor

    def canvas_radius(self, opts: LayoutOpts) -> float:
        box = self.bounding_box(opts)
        return max(corner.length for corner in box.corners)

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        return BoundingBox(self.corner_a, self.corner_b)

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        box = self.bounding_box(opts)
        canvas.add_to(
            L_BACKGROUND,
            dw.Rectangle(
                box.corner_bl.x,
                box.corner_bl.y,
                height=box.height,
                width=box.width,
                rx=BACKGROUND_RADIUS,
                fill=self.color,
                stroke_width=0,
            ),
        )


@dataclass
class TextBox(Element):
    """
    A textbox.
    """

    position: Vec2  # left center
    text: str

    def canvas_radius(self, opts: LayoutOpts) -> float:
        # this is a horrible approximation, but figuring out the exact
        # dimensions of the finished rendered text is just not worth
        # the effort
        return self.bounding_box(opts).canvas_radius()

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        # this is a horrible approximation, but figuring out the exact
        # dimensions of the finished rendered text is just not worth
        # the effort
        length = TEXT_FONT_SIZE * len(self.text)
        top_left = Vec2(self.position.x, self.position.y + TEXT_FONT_SIZE)
        bottom_right = Vec2(self.position.x + length, self.position.y - TEXT_FONT_SIZE)
        return BoundingBox(top_left, bottom_right)

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        canvas.add_to(
            L_TEXT,
            dw.Text(
                self.text,
                TEXT_FONT_SIZE,
                self.position.x,
                self.position.y,
                text_anchor="start",
                dominant_baseline="central",
            ),
        )


@dataclass
class MetaElement(Element):
    """
    An element consisting of other elements.
    """

    @abstractmethod
    def build(self, opts: LayoutOpts) -> List[Element]:
        """
        Get the atomic constituent elements that make up this element.
        """
        return NotImplemented

    def canvas_radius(self, opts: LayoutOpts) -> float:
        return max(element.canvas_radius(opts) for element in self.build(opts))

    def bounding_box(self, opts: LayoutOpts) -> BoundingBox:
        box = BoundingBox()
        for element in self.build(opts):
            box = box.union(element.bounding_box(opts))

        return box

    def draw(self, canvas: LayeredCanvas, opts: LayoutOpts) -> None:
        for element in self.build(opts):
            element.draw(canvas, opts)


@dataclass
class GoalElement(MetaElement):
    """
    A graphic element representing a pachisi player's goal on the board.
    """

    goal: Group
    anchor: Vec2
    direction: Vec2

    def build(self, opts: LayoutOpts) -> List[Element]:
        elements: List[Element] = []

        if len(self.goal) == 0:
            return elements

        for i, field in enumerate(self.goal.fields, 1):
            position = self.anchor + i * self.direction * GRID
            elements.append(FieldElement(field, position))

        if self.goal.ordered:
            elements.append(Line(self.anchor, position))

        elements.append(BackgroundLine(self.anchor, position, self.goal.background_color))
        return elements


@dataclass
class HomeElement(MetaElement):
    """
    A graphic element representing a pachisi player's home on the board.
    """

    home: Group
    size: int
    position: int
    inner_box: BoundingBox
    # Positions around the board for placing player's homes
    # 7 0 1
    # 6   2
    # 5 4 3

    def anchor(self) -> Vec2:
        """
        Find the center of the top-left field in the home.
        """
        size = (self.size - 1) * GRID
        x_min = self.inner_box.corner_bl.x
        y_min = self.inner_box.corner_bl.y
        x_center = self.inner_box.center.x
        y_center = self.inner_box.center.y
        x_max = self.inner_box.corner_tr.x
        y_max = self.inner_box.corner_tr.y

        # fmt: off
        return [
            Vec2(x_center - size / 2,              y_max + BACKGROUND_RADIUS + size),
            Vec2(x_max + BACKGROUND_RADIUS,        y_max + BACKGROUND_RADIUS + size),
            Vec2(x_max + BACKGROUND_RADIUS,        y_center + size / 2),
            Vec2(x_max + BACKGROUND_RADIUS,        y_min - BACKGROUND_RADIUS),
            Vec2(x_center - size / 2,              y_min - BACKGROUND_RADIUS),
            Vec2(x_min - BACKGROUND_RADIUS - size, y_min - BACKGROUND_RADIUS),
            Vec2(x_min - BACKGROUND_RADIUS - size, y_center + size / 2),
            Vec2(x_min - BACKGROUND_RADIUS - size, y_max + BACKGROUND_RADIUS + size),
        ][self.position]
        # fmt: on

    def build(self, opts: LayoutOpts) -> List[Element]:
        elements: List[Element] = []

        anchor = self.anchor()
        size = (self.size - 1) * GRID
        corner_a = anchor + Vec2(-BACKGROUND_RADIUS, BACKGROUND_RADIUS)
        corner_b = anchor + Vec2(size + BACKGROUND_RADIUS, -(size + BACKGROUND_RADIUS))
        elements.append(BackgroundRect(corner_a, corner_b, self.home.background_color))

        for i in range(self.size):
            for j in range(self.size):
                index = j + i * self.size
                if index >= len(self.home.fields):
                    continue
                field = self.home.fields[index]
                position = anchor + Vec2(j * GRID, -i * GRID)
                elements.append(FieldElement(field, position))

        return elements


@dataclass
class LoopElement(MetaElement):
    """
    An Element representing the board's main loop of fields.
    Includes shortcuts.
    """

    loop: List[Field]
    shortcuts: List[Tuple[int, int]]

    def wheel_ok(self) -> bool:
        """
        Whether wheel layout is available for this loop.
        """
        return len(self.shortcuts) == 0

    @property
    def inter_field_angle(self) -> float:
        """
        The angle between two fields on the loop.
        """
        return 2 * math.pi / len(self.loop)

    @property
    def radius(self) -> float:
        """
        The loop's radius (for the line on which all fields are placed).
        """
        # See: https://en.wikipedia.org/wiki/Chord_(geometry)
        return GRID / (2 * math.sin(self.inter_field_angle / 2))

    def angle(self, field_index: int) -> float:
        """
        The angle at which the n-th field will be placed.
        """
        return field_index * self.inter_field_angle

    def position(self, field_index: int) -> Vec2:
        """
        The position in which the n-th field will be placed.
        """
        return Vec2.from_radial(self.radius, self.angle(field_index))

    def build(self, opts: LayoutOpts) -> List[Element]:
        loop_elements = [
            FieldElement(field, self.position(i)) for i, field in enumerate(self.loop)
        ]
        shortcut_elements = [
            ShortcutElement(self.position(i), self.position(j)) for i, j in self.shortcuts
        ]
        line = Circle(Vec2(0, 0), self.radius)
        return loop_elements + shortcut_elements + [line]


@dataclass
class GoalsElement(MetaElement):
    """
    An element containing all goals.
    """

    goals: Dict[int, Group]
    loop_element: LoopElement  # to know where to layout the goals
    force_sun: bool = False

    def wheel_ok(self) -> bool:
        """
        Whether wheel layout is available with these goals in the given
        loop.
        """
        max_goal_size = max(len(goal) for goal in self.goals.values())
        return (
            self.loop_element.wheel_ok()
            and (max_goal_size + 1) * GRID + EPSILON <= self.loop_element.radius
        )

    def build(self, opts: LayoutOpts) -> List[Element]:
        sun = 1 if self.force_sun or not self.wheel_ok() else -1
        return [
            GoalElement(
                goal,
                self.loop_element.position(i),
                sun * self.loop_element.position(i).normalized(),
            )
            for i, goal in self.goals.items()
        ]


@dataclass
class InnerBoardElement(MetaElement):
    """
    An element containing the inner board (loop and goals)
    """

    loop: List[Field]
    goals: Dict[int, Group]
    shortcuts: List[Tuple[int, int]]
    force_sun: bool = False

    def angle(self, field_index) -> float:
        """
        The angle at which the n-th field will be placed.
        """
        loop = LoopElement(self.loop, self.shortcuts)
        return loop.angle(field_index)

    def build(self, opts: LayoutOpts) -> List[Element]:
        loop = LoopElement(self.loop, self.shortcuts)
        goals = GoalsElement(self.goals, loop, self.force_sun)
        return [loop, goals]


@dataclass
class HomesElement(MetaElement):
    """
    An element containing all homes.
    """

    homes: Dict[int, Group]
    inner: InnerBoardElement  # to know where to layout the homes

    def build(self, opts: LayoutOpts) -> List[Element]:
        home_positions = copy.deepcopy(COUNT_TO_POSITIONS[len(self.homes)])
        home_angles = [pos / 4 * math.pi for pos in home_positions]
        max_home_size = max(len(home) for home in self.homes.values())
        home_size = math.ceil(math.sqrt(max_home_size))
        inner_box = self.inner.bounding_box(opts)
        inner_box.extend_by(HOME_PADDING)

        elements: List[Element] = []
        for hook, group in self.homes.items():
            # find the closest valid home position by comparing its
            # circular coordinate angle to the home's angle
            angle = self.inner.angle(hook)
            bias = 1e-3
            distances = [abs(angle + bias - home_angle) for home_angle in home_angles]
            min_index = distances.index(min(distances))
            position = home_positions[min_index]
            del home_angles[min_index]
            del home_positions[min_index]

            elements.append(HomeElement(group, home_size, position, inner_box))

        return elements


@dataclass
class MarkElement(MetaElement):
    """
    An Element containing the symbol and description of a single mark.
    """

    mark: FieldMark
    position: Vec2

    def build(self, opts: LayoutOpts) -> List[Element]:
        field = FieldElement(Field(mark=self.mark), self.position)
        text_position = self.position + Vec2(FIELD_RADIUS + FIELD_MARGIN, 0)
        text_content = self.mark.name
        if self.mark.description:
            text_content += ": " + self.mark.description
        text = TextBox(text_position, text_content)
        return [field, text]


@dataclass
class MarksElement(MetaElement):
    """
    An Element containing the symbols and descriptions of all marks on
    the board.
    """

    marks: List[FieldMark]
    anchor: Vec2

    def build(self, opts: LayoutOpts) -> List[Element]:
        position = self.anchor + Vec2(FIELD_RADIUS, -FIELD_RADIUS)
        distance = 2 * FIELD_RADIUS + 2 * FIELD_MARGIN
        return [
            MarkElement(mark, position + Vec2(0, -i * distance))
            for i, mark in enumerate(self.marks)
        ]


@dataclass
class BoardElement(MetaElement):
    """
    An Element representing the graphic elements of an entire pachisi
    board.
    """

    board: Board
    layout: Layout

    def build(self, opts: LayoutOpts) -> List[Element]:
        inner = InnerBoardElement(
            self.board.loop,
            self.board.goals,
            self.board.shortcuts,
            self.layout == Layout.SUN,
        )
        homes = HomesElement(self.board.homes, inner)

        elements: List[Element] = [inner, homes]
        if opts.show_mark_explanation:
            elements.append(
                MarksElement(
                    self.board.marks,
                    homes.bounding_box(opts).corner_bl
                    + Vec2(BACKGROUND_RADIUS - FIELD_RADIUS, -FIELD_MARGIN),
                )
            )
        return elements

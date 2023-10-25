"""
This module contains a renderer for pachisi boards.
"""
from typing import Optional, Union

import drawsvg as dw  # type: ignore

from pachisi_render.renderer.board import Board
from pachisi_render.renderer.layout import BoardElement, LayeredCanvas, LayoutOpts, Vec2


# pylint: disable-next=too-few-public-methods
class Renderer:
    """
    Renders a pachisi-board
    """

    def render(  # pylint: disable=too-many-arguments
        self,
        board: Board,
        opts: LayoutOpts = LayoutOpts(),
        out: Optional[str] = None,
    ) -> Union[str, None]:
        """
        Render the given board state into an svg and return the svg's
        content as a string.
        """
        canvas = LayeredCanvas()
        element = BoardElement(board, opts.layout)

        box = element.bounding_box(opts)
        origin = Vec2(-box.width / 2, -box.height / 2) + box.center
        context = dw.Context(invert_y=True)
        drawing = dw.Drawing(box.width, box.height, origin=(origin.x, origin.y), context=context)

        element.draw(canvas, opts)
        canvas.draw(drawing)
        if out is not None:
            with open(out, "w", encoding="utf-8") as output_file:
                return drawing.as_svg(output_file=output_file)
        else:
            return drawing.as_svg()

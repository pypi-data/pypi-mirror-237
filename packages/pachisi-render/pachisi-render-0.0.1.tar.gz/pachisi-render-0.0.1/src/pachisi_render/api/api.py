"""
This module contains the pachisi render api.
"""

from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse

from pachisi_render.api.board_adapter import BoardAdapter
from pachisi_render.api.state import BoardState
from pachisi_render.renderer.renderer import Renderer

DESCRIPTION = """
Pachisi Render allows you to render a pachisi board according to a board state
provided by you.
"""

app = FastAPI(
    title="pachisi-render",
    description=DESCRIPTION,
    summary="Easily render a simple, yet customizable pachisi board as an svg.",
    version="0.0.1",
)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    """
    Redirect users to /docs on first visit.
    """
    return RedirectResponse(url="/docs")


@app.post(
    "/board",
    responses={200: {"content": {"image/svg+xml": {}}}},
    response_class=Response,
)
async def board(state: BoardState):
    """
    This endpoint takes a pachisi board's state as input, renders a
    board with the given state as an svg and returns the svg to the
    caller.
    """
    adapter = BoardAdapter(state).convert()
    svg = Renderer().render(adapter)
    assert svg is not None
    return Response(content=svg, media_type="image/svg+xml")

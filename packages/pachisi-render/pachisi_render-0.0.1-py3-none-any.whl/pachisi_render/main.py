"""
This module is the script for running the pachisi render API server.
"""
import argparse

import uvicorn


def main():
    """
    Entry point for running the API as its own server.
    """
    parser = argparse.ArgumentParser(
        prog="PachisiRender",
        description="Start a server providing a REST API for rendering a pachisi board.",
        epilog="For help on API usage, start the server and visit its /docs page",
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default="8000", type=int)
    args = parser.parse_args()
    uvicorn.run("pachisi_render.api.api:app", host=args.host, port=args.port)


if __name__ == "__main__":
    main()

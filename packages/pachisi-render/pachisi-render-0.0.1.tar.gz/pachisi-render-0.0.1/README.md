# Pachisi Render
Easily render a simple, yet customizable pachisi board as an svg.

# Usage
After installation, start the tool via the `pachisi-render` command.
This starts a webserver, which provides a single REST API endpoint at `/board`.
Send an HTTP request containing a json-encoded description of the state of a
pachisi board to this endpoint and it will return an SVG image showing a pachisi
board in the provided state.

Details on the API are provided in the documentation, which is included with the
tool and can be found at the `/docs` url.

# Maintenance
This tool was developed and is being maintained by the Institute of Telematics
at the Karlsruhe Institute of Technology for use in it's protocol engineering
course.

# License
Copyright Karlsruhe Institute of Technology, Institute of Telematics, 2023

Distributed under the terms of the MIT license.

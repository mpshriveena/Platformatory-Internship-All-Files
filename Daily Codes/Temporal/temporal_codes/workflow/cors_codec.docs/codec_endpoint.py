"""Temporal Python Codec Server

Usage:
  codec_server.py
  codec_server.py --web <url>

Options:
  --web    Temporal Web UI URL to enable CORS for

"""
import logging
from functools import partial
from typing import Awaitable, Callable, Iterable, List

from aiohttp import hdrs, web
from google.protobuf import json_format
from temporalio.api.common.v1 import Payload, Payloads
from docopt import docopt

from codec import EncryptionCodec

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def build_codec_server(arguments) -> web.Application:
    async def header_options(req: web.Request) -> web.Response:
        logger.debug(f"Received OPTIONS request at {req.path}")
        resp = web.Response()
        if arguments["--web"]==True:
            if req.headers.get(hdrs.ORIGIN) == arguments["<url>"]:
                resp.headers[hdrs.ACCESS_CONTROL_ALLOW_ORIGIN] = arguments["<url>"]
                resp.headers[hdrs.ACCESS_CONTROL_ALLOW_METHODS] = "POST"
                resp.headers[hdrs.ACCESS_CONTROL_ALLOW_HEADERS] = "content-type,x-namespace"
        return resp

    async def apply(
        fn: Callable[[Iterable[Payload]], Awaitable[List[Payload]]], req: web.Request
    ) -> web.Response:
        logger.debug(f"Received request at {req.path}")
        logger.debug(f"Request headers: {req.headers}")
        
        body = await req.read()
        logger.debug(f"Request body: {body.decode()}")

        assert req.content_type == "application/json", f"Expected content-type application/json, got {req.content_type}"
        payloads = json_format.Parse(body, Payloads())

        try:
            payloads = Payloads(payloads=await fn(payloads.payloads))
        except Exception as e:
            logger.error(f"Error processing payloads: {str(e)}")
            return web.Response(status=500, text=str(e))

        resp = await header_options(req)
        resp.content_type = "application/json"
        resp.text = json_format.MessageToJson(payloads)
        logger.debug(f"Response: {resp.text}")
        return resp

    app = web.Application()
    codecs = {"default": EncryptionCodec()}
    for route, codec in codecs.items():
        app.add_routes(
            [
                web.post(("/" + route + "/encode"), partial(apply, codec.encode)),
                web.post(("/" + route + "/decode"), partial(apply, codec.decode)),
                web.options(("/" + route + "/decode"), header_options),
            ]
        )
    return app

if __name__ == "__main__":
    arguments = docopt(__doc__)
    logger.info("Starting codec server on http://127.0.0.1:8081")
    web.run_app(build_codec_server(arguments), host="127.0.0.1", port=8081)
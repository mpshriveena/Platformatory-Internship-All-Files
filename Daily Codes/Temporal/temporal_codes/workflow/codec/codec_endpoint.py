import logging
from functools import partial
from typing import Awaitable, Callable, Iterable, List

from aiohttp import hdrs, web
from google.protobuf import json_format
from temporalio.api.common.v1 import Payload, Payloads

from codec import EncryptionCodec

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def build_codec_server() -> web.Application:
    async def header_options(req: web.Request) -> web.Response:
        logger.debug(f"Received OPTIONS request at {req.path}")
        resp = web.Response()
        return resp

    # General purpose payloads-to-payloads
    async def apply(
        fn: Callable[[Iterable[Payload]], Awaitable[List[Payload]]], req: web.Request
    ) -> web.Response:
        logger.debug(f"Received request at {req.path}")
        logger.debug(f"Request headers: {req.headers}")
        
        body = await req.read()
        logger.debug(f"Request body: {body.decode()}")

        # Read payloads as JSON
        assert req.content_type == "application/json", f"Expected content-type application/json, got {req.content_type}"
        payloads = json_format.Parse(body, Payloads())

        # Apply
        try:
            payloads = Payloads(payloads=await fn(payloads.payloads))
        except Exception as e:
            logger.error(f"Error processing payloads: {str(e)}")
            return web.Response(status=500, text=str(e))

        # Apply headers and return JSON
        resp = await header_options(req)
        resp.content_type = "application/json"
        resp.text = json_format.MessageToJson(payloads)
        logger.debug(f"Response: {resp.text}")
        return resp

    # Build app per-Namespace
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
    logger.info("Starting codec server on http://127.0.0.1:8081")
    web.run_app(build_codec_server(), host="127.0.0.1", port=8081)
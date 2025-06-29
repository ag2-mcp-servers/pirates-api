# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T19:18:00+00:00



import argparse
import json
import os
from typing import *
from typing import Optional

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

app = MCPProxy(
    contact={'name': 'Fun Generators', 'url': 'http://fungenerators.com/api/pirate/'},
    description='Ahoy matey! We help the landlubbers to get to know about the seamen way! You can generate pirate names, get some real pirate insults and pirate filler text. Oh you can translate to pirate lingo as well. [Click here to subscribe](http://fungenerators.com/api/pirate/) \n',
    termsOfService='https://fungenerators.com/terms',
    title='Pirates API',
    version='1.5',
    servers=[
        {'url': 'http://api.fungenerators.com'},
        {'url': 'https://api.fungenerators.com'},
    ],
)


@app.get(
    '/pirate/generate/insult',
    description=""" Generate random pirate insults. """,
    tags=['pirate_text_generation', 'pirate_lingo_translation'],
    security=[
        APIKeyHeader(name="X-Fungenerators-Api-Secret"),
    ],
)
def get_pirate_generate_insult(limit: Optional[int] = None):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/pirate/generate/lorem-ipsum',
    description=""" Generate pirate lorem ipsum. """,
    tags=['pirate_text_generation', 'pirate_lingo_translation'],
    security=[
        APIKeyHeader(name="X-Fungenerators-Api-Secret"),
    ],
)
def get_pirate_generate_lorem_ipsum(
    type: Optional[str] = None, limit: Optional[int] = None
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/pirate/generate/name',
    description=""" Generate random pirate names. """,
    tags=['pirate_text_generation', 'pirate_lingo_translation'],
    security=[
        APIKeyHeader(name="X-Fungenerators-Api-Secret"),
    ],
)
def get_pirate_generate_name(
    variation: Optional[str] = None, limit: Optional[int] = None
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/pirate/translate',
    description=""" Translate from English to pirate. """,
    tags=['pirate_lingo_translation'],
    security=[
        APIKeyHeader(name="X-Fungenerators-Api-Secret"),
    ],
)
def get_pirate_translate(text: str):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)

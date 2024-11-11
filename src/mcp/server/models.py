"""
This module provides simpler types to use with the server for managing prompts
and tools.
"""

from dataclasses import dataclass
from typing import Literal

from pydantic import BaseModel

from mcp.types import (
    ServerCapabilities,
)


class InitializationOptions(BaseModel):
    server_name: str
    server_version: str
    capabilities: ServerCapabilities

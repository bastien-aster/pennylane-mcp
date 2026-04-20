"""Decorator-based tool registry.

Each tool module decorates its async handler with @tool(...) to register it
without touching server.py. The server iterates TOOLS at startup and can
filter by resource (see _metadata.py for profile definitions).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Awaitable, Callable

Handler = Callable[..., Awaitable[Any]]


@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    input_schema: dict[str, Any]
    resource: str
    readonly: bool
    handler: Handler


TOOLS: list[ToolSpec] = []
_NAMES: set[str] = set()


def tool(
    *,
    name: str,
    description: str,
    input_schema: dict[str, Any],
    resource: str,
    readonly: bool = False,
) -> Callable[[Handler], Handler]:
    """Register an async handler as an MCP tool.

    readonly=True flags safe GET-equivalent operations for the
    PENNYLANE_READONLY filter.
    """
    def decorator(fn: Handler) -> Handler:
        if name in _NAMES:
            raise RuntimeError(f"Duplicate tool name: {name}")
        _NAMES.add(name)
        TOOLS.append(
            ToolSpec(
                name=name,
                description=description,
                input_schema=input_schema,
                resource=resource,
                readonly=readonly,
                handler=fn,
            )
        )
        return fn

    return decorator

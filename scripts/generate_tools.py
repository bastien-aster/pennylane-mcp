"""Generate MCP tool modules from the Pennylane OpenAPI spec.

Usage:
    python scripts/generate_tools.py

Reads docs/pennylane-openapi.json and overwrites src/pennylane_mcp/tools/*.py
(except _registry.py and __init__.py, which are handwritten).

Each generated module contains one handler per operation. Handlers register
themselves via the @tool decorator from _registry.
"""
from __future__ import annotations

import json
import pprint
import re
import sys
from pathlib import Path
from collections import defaultdict

# Resources to skip entirely — Make handles these for us.
SKIP_RESOURCES = {"webhook_subscription"}

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

# Import after sys.path setup so we can pull resource metadata from the
# shipped package (single source of truth for profile / label / keywords).
from pennylane_mcp._metadata import RESOURCE_METADATA, resource_to_profile  # noqa: E402

SPEC_PATH = REPO_ROOT / "docs" / "pennylane-openapi.json"
TOOLS_DIR = REPO_ROOT / "src" / "pennylane_mcp" / "tools"

MODULE_HEADER = '''"""Auto-generated from docs/pennylane-openapi.json. Do not edit by hand.

Regenerate with: python scripts/generate_tools.py
"""
from typing import Any, Optional

from .._registry import tool
from ..client import PennylaneClient


'''


def camel_to_snake(name: str) -> str:
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()


def clean_name(name: str) -> str:
    """Make a valid Python identifier."""
    name = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if name and name[0].isdigit():
        name = "_" + name
    return name


def resource_of_path(path: str) -> str:
    """Extract the logical resource name from an API path."""
    segs = [s for s in path.split("/") if s and not s.startswith("{")]
    if "external" in segs:
        i = segs.index("external")
        segs = segs[i + 2:]
    return segs[0].replace("-", "_") if segs else "misc"


def build_input_schema(op: dict, spec: dict) -> tuple[dict, list[str], list[str]]:
    """Return (json_schema, path_params, query_params) for an operation."""
    props: dict[str, dict] = {}
    required: list[str] = []
    path_params: list[str] = []
    query_params: list[str] = []

    for p in op.get("parameters", []):
        name = p.get("name")
        if not name:
            continue
        p_in = p.get("in")
        schema = p.get("schema", {}) or {}
        p_type = schema.get("type", "string")
        description = p.get("description", "") or ""
        prop: dict = {"type": p_type}
        if description:
            prop["description"] = description[:300]
        enum = schema.get("enum")
        if enum:
            prop["enum"] = enum
        props[name] = prop
        if p_in == "path":
            path_params.append(name)
            required.append(name)
        elif p_in == "query":
            query_params.append(name)
            if p.get("required"):
                required.append(name)

    rb = op.get("requestBody", {}) or {}
    if rb:
        props["body"] = {
            "type": "object",
            "description": "Request body payload. See the Pennylane API reference for the exact schema of this endpoint.",
            "additionalProperties": True,
        }
        if rb.get("required"):
            required.append("body")

    schema = {"type": "object", "properties": props}
    if required:
        schema["required"] = required
    return schema, path_params, query_params


def enrich_description(
    *,
    summary: str,
    description: str,
    operation_id: str,
    resource: str,
) -> str:
    """Build a rich description: [Profile · Label] Summary. Description. [Keywords FR: ...]

    Claude matches tool selection on the full description, so we front-load the
    domain label and weave French keywords in so French-speaking users' intent
    lines up naturally without translating every API summary.
    """
    meta = RESOURCE_METADATA.get(resource, {})
    profile = resource_to_profile(resource).capitalize()
    label_en = meta.get("label_en") or resource.replace("_", " ").title()
    label_fr = meta.get("label_fr") or label_en
    keywords_fr = meta.get("keywords_fr") or []

    safe_summary = (summary or operation_id).replace('"', "'")
    long_desc = description or ""
    long_desc = long_desc.replace('"', "'").replace("\n", " ").strip()
    long_desc = re.sub(r"\s+", " ", long_desc)
    if len(long_desc) > 400:
        long_desc = long_desc[:397] + "..."

    parts = [f"[{profile} · {label_en} / {label_fr}] {safe_summary}"]
    if long_desc and long_desc.lower() != safe_summary.lower():
        parts.append(long_desc)
    if keywords_fr:
        parts.append(f"Mots-clés FR: {', '.join(keywords_fr)}.")
    return " ".join(parts)


def generate_handler(
    *,
    tool_name: str,
    operation_id: str,
    summary: str,
    description: str,
    method: str,
    path: str,
    resource: str,
    input_schema: dict,
    path_params: list[str],
    query_params: list[str],
    has_body: bool,
) -> str:
    """Emit a Python function body that calls the API and registers as a tool."""
    fn_name = clean_name(camel_to_snake(operation_id))
    full_desc = enrich_description(
        summary=summary,
        description=description,
        operation_id=operation_id,
        resource=resource,
    )

    # pprint emits valid Python (True/False/None) rather than JSON literals.
    schema_repr = pprint.pformat(input_schema, indent=4, width=100, sort_dicts=False)
    schema_repr = "\n".join("    " + line if i else line for i, line in enumerate(schema_repr.splitlines()))

    path_format_args = ", ".join(f"{p}={p}" for p in path_params)
    query_dict_entries = ", ".join(f"{repr(q)}: {q}" for q in query_params)

    # Strip the shared /api/external/v2 prefix — the client's base_url already includes it.
    trimmed_path = path
    if trimmed_path.startswith("/api/external/v2"):
        trimmed_path = trimmed_path[len("/api/external/v2"):] or "/"

    path_lines = []
    if path_params:
        path_lines.append(f'    url = f"{trimmed_path}".format({path_format_args})')
    else:
        path_lines.append(f'    url = "{trimmed_path}"')

    params_lines = []
    if query_params:
        params_lines.append(f"    params = {{{query_dict_entries}}}")
        params_lines.append("    params = {k: v for k, v in params.items() if v is not None}")
    else:
        params_lines.append("    params = None")

    call_line: str
    if method == "get":
        call_line = "    return await client.get(url, params=params)"
    elif method == "delete":
        call_line = "    return await client.delete(url)"
    elif method == "post":
        call_line = "    return await client.post(url, data=body)"
    elif method == "put":
        call_line = "    return await client.put(url, data=body)"
    else:
        call_line = "    raise NotImplementedError"

    sig_parts = []
    sig_parts.append("client: PennylaneClient")
    for p in path_params:
        sig_parts.append(f"{p}: str")
    for q in query_params:
        sig_parts.append(f"{q}: Optional[Any] = None")
    if has_body:
        sig_parts.append("body: Optional[dict[str, Any]] = None")
    signature = ",\n    ".join(sig_parts)

    return (
        f"@tool(\n"
        f"    name=\"{tool_name}\",\n"
        f"    description={json.dumps(full_desc, ensure_ascii=False)},\n"
        f"    input_schema={schema_repr},\n"
        f"    resource=\"{resource}\",\n"
        f")\n"
        f"async def {fn_name}(\n    {signature},\n) -> Any:\n"
        f"{path_lines[0]}\n"
        f"{params_lines[0]}\n"
        + (f"{params_lines[1]}\n" if len(params_lines) > 1 else "")
        + f"{call_line}\n\n\n"
    )


def main() -> None:
    spec = json.loads(SPEC_PATH.read_text())
    paths = spec.get("paths", {})

    by_resource: dict[str, list[str]] = defaultdict(list)
    tool_count = 0
    skipped = 0

    for path, methods in paths.items():
        resource = resource_of_path(path)
        if resource in SKIP_RESOURCES:
            skipped += sum(1 for m in methods if m in ("get", "post", "put", "delete"))
            continue
        for method, op in methods.items():
            method = method.lower()
            if method not in ("get", "post", "put", "delete"):
                continue
            op_id = op.get("operationId") or f"{method}_{resource}_{tool_count}"
            tool_name = f"pennylane_{clean_name(camel_to_snake(op_id))}"
            summary = op.get("summary") or ""
            description = op.get("description") or ""
            input_schema, path_params, query_params = build_input_schema(op, spec)
            has_body = "body" in input_schema["properties"]
            code = generate_handler(
                tool_name=tool_name,
                operation_id=op_id,
                summary=summary,
                description=description,
                method=method,
                path=path,
                resource=resource,
                input_schema=input_schema,
                path_params=path_params,
                query_params=query_params,
                has_body=has_body,
            )
            by_resource[resource].append(code)
            tool_count += 1

    TOOLS_DIR.mkdir(parents=True, exist_ok=True)

    # Remove stale hand-written tool modules (we regenerate them all)
    preserved = {"_registry.py", "__init__.py"}
    for f in TOOLS_DIR.glob("*.py"):
        if f.name not in preserved:
            f.unlink()

    modules = []
    for resource, snippets in sorted(by_resource.items()):
        filename = f"{resource}.py"
        body = MODULE_HEADER + "".join(snippets)
        (TOOLS_DIR / filename).write_text(body)
        modules.append(resource)

    # Write __init__ that imports every module so decorators run
    init_body = '"""Pennylane MCP tools — auto-imported on package load to register handlers."""\n\n'
    for mod in modules:
        init_body += f"from . import {mod}  # noqa: F401\n"
    (TOOLS_DIR / "__init__.py").write_text(init_body)

    print(f"Generated {tool_count} tools across {len(modules)} modules.")
    print(f"Skipped {skipped} operations from: {', '.join(sorted(SKIP_RESOURCES))}")


if __name__ == "__main__":
    main()

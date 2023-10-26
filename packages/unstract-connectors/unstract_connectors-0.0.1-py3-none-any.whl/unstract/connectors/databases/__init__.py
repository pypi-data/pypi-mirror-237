from typing import Any

from unstract.connectors.databases.register import register_connectors

connectors: dict[str, Any] = {}
register_connectors(connectors)

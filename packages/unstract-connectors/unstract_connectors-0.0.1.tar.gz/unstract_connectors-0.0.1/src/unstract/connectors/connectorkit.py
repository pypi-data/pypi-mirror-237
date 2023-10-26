import inspect
import logging
import pkgutil
from typing import Any, Optional

import unstract.connectors.databases
import unstract.connectors.filesystems
from unstract.connectors.base import UnstractConnector

logger = logging.getLogger(__name__)


class Connectorkit:
    def __init__(self) -> None:
        self.built_in_connectors = []
        self.connectorkit_dict = {}
        self.connector_connector_mappping = {}
        self.connector_id_connector_mappping = {}
        logger.debug("Loading built-in connectors(databases)...")
        for package in pkgutil.walk_packages(unstract.connectors.databases.__path__):
            if package.ispkg:
                self.built_in_connectors.append(package.name)
        logger.debug("Loading built-in connectors(filesystems)...")
        for package in pkgutil.walk_packages(unstract.connectors.filesystems.__path__):
            if package.ispkg:
                self.built_in_connectors.append(package.name)
        logger.debug(f"Found built-in connectors : {self.built_in_connectors}")

        for connector in self.built_in_connectors:
            try:
                connector_module = __import__(
                    f"unstract.connectors.databases.{connector}.{connector}",
                    fromlist=[connector],
                )
            except ModuleNotFoundError:
                try:
                    connector_module = __import__(
                        f"unstract.connectors.filesystems.{connector}.{connector}",
                        fromlist=[connector],
                    )
                except ModuleNotFoundError:
                    continue
            classes = [
                class_
                for class_ in dir(connector_module)
                if inspect.isclass(getattr(connector_module, class_))
            ]
            for class_ in classes:
                if (
                    issubclass(getattr(connector_module, class_), UnstractConnector)
                    and class_ != "UnstractConnector"
                    and class_ != "UnstractDB"
                    and class_ != "UnstractFileSystem"
                ):
                    # We are adding an instance of the connector to the
                    # connectorkit_dict.
                    # We can directly call methods like this:
                    # self.connectorkit_dict["connector_name"].get_name()
                    logging.debug(
                        f"Adding built-in connector '{class_}' to connectorkit"
                    )
                    self.connectorkit_dict[class_] = getattr(connector_module, class_)
                    connector_name = getattr(connector_module, class_).get_name()
                    connector_id = getattr(connector_module, class_).get_id()
                    self.connector_connector_mappping[connector_name] = class_
                    self.connector_id_connector_mappping[connector_id] = class_
        logger.debug(f"Found the following connectors : {self.connectorkit_dict}")

    def get_connector_class_for_connector_name(
        self, connector_name: str
    ) -> Optional[str]:
        if connector_name in self.connector_connector_mappping:
            return self.connector_connector_mappping[connector_name]
        else:
            return None

    def get_connector_class_for_connector_id(self, connector_id: str) -> Optional[str]:
        if connector_id in self.connector_id_connector_mappping:
            return self.connector_id_connector_mappping[connector_id]
        else:
            return None

    def get_connector(self, connector_name: str) -> Optional[UnstractConnector]:
        if connector_name in self.connectorkit_dict:
            return self.connectorkit_dict[connector_name]
        else:
            logging.error(f">> Connector '{connector_name}' not found in connectorkit")
            logging.error(
                f">> Connectors in connectorkit : {self.connectorkit_dict.keys()}"
            )
            return None

    def get_connector_by_id(
        self, connector_id: str, *args: Any, **kwargs: Any
    ) -> UnstractConnector:
        """Instantiates and returns a connector.

        Args:
            connector_id (str): Identifies connector to create

        Raises:
            RuntimeError: If the ID is invalid/connector is missing

        Returns:
            UnstractConnector: Concrete impl of the `UnstractConnector` base
        """
        connector_class = self.get_connector(
            self.get_connector_class_for_connector_id(connector_id) or ""
        )
        if connector_class is None:
            raise RuntimeError(f"Couldn't obtain connector for {connector_id}")
        return connector_class(*args, **kwargs)

    def get_connectors_list(self) -> list[dict[str, Any]]:
        connectors = []
        for connector in self.connectorkit_dict:
            m = self.connectorkit_dict[connector]
            _id = m.get_id()
            name = m.get_name()
            json_schema = m.get_json_schema()
            desc = m.get_description()
            icon = m.get_icon()
            oauth = m.requires_oauth()
            python_social_auth_backend = m.python_social_auth_backend()
            can_read = m.can_read()
            can_write = m.can_write()
            connector_mode = m.get_connector_mode()
            connectors.append(
                {
                    "id": _id,
                    "name": name,
                    "class_name": m.__name__,
                    "description": desc,
                    "icon": icon,
                    "type": "built-in-file",
                    "oauth": oauth,
                    "python_social_auth_backend": python_social_auth_backend,  # noqa
                    "can_read": can_read,
                    "can_write": can_write,
                    "json_schema": json_schema,
                    "connector_mode": connector_mode,
                }
            )
        return connectors

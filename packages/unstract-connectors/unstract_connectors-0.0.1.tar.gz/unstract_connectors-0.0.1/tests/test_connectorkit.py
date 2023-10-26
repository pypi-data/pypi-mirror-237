import unittest

from unstract.connectors.connectorkit import Connectorkit
from unstract.connectors.enums import ConnectorModes


import logging
logger = logging.getLogger("unstract.connectors")
logger.setLevel(logging.DEBUG)
class ConnectorkitTestCase(unittest.TestCase):
    def test_connectorkit(self):
        connectorkit = Connectorkit()
        c_class = connectorkit.get_connector_class_for_connector_name("Snowflake")
        self.assertEqual(c_class, "SnowflakeDB")

        c = connectorkit.get_connector("SnowflakeDB")
        self.assertEqual(c.get_connector_mode(), ConnectorModes.DATABASE)

        c = connectorkit.get_connector("MinioFS")
        self.assertEqual(c.get_connector_mode(), ConnectorModes.FILE_SYSTEM)


if __name__ == "__main__":
    unittest.main()

import unittest

from server import app
from model import db, connect_to_db


class ServerTests(unittest.TestCase):
    """Tests for my PetShare site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        """Test index page loads correctly."""

        result = self.client.get("/")
        self.assertIn("Find your furry BFF", result.data)


if __name__ == "__main__":
    unittest.main()

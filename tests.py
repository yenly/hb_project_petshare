import unittest
# import doctest
import server

from server import app
from model import db, connect_to_db, test_data
# from flask import Flask
# from flask_mail import Mail, Message


class ServerTests(unittest.TestCase):
    """Tests for my PetShare site."""

    def setUp(self):
        self.client = app.test_client()
        # self.app = Flask(__name__)
        # self.mail = Mail(self.app)
        app.config['TESTING'] = True

        with self.client as c:
            with c.session_transaction() as session:
                session['user_id'] = 1
                session['user_city'] = "San Francisco"

    def test_index(self):
        """Test index page loads correctly."""

        result = self.client.get("/")
        self.assertIn("Find your furry BFF", result.data)


class ServerTestsDatabase(unittest.TestCase):
    """Flask tests that uses petshare database."""

    def setUp(self):
        """Set up env for every test before testing db."""
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
            with c.session_transaction() as session:
                session['user_id'] = 1
                session['user_city'] = "San Francisco"

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")
        db.create_all()
        test_data()

    def tearDown(self):
        """Clean env after every test."""

        db.session.close()
        db.drop_all()

    def test_user_profile(self):
        """Test User profile loads successfully."""

        result = self.client.get('/user/1')
        self.assertEquals(200, result.status_code)
        self.assertIn("Charlie Brown", result.data)

    def test_pet_profile(self):
        """Test pet profile loads successfully."""

        result = self.client.get('/pet_profile/1')
        self.assertEquals(200, result.status_code)
        self.assertIn("Snoopy", result.data)

    def test_login(self):
        """Test user logged and redirect to member dashboard."""

        result = self.client.post('/login',
                                  data={"email": "charlie@gmail.com",
                                        "password": "123xyz"},
                                  follow_redirects=True)

        self.assertEquals(200, result.status_code)
        self.assertIn("Charlie", result.data)

    def test_petmapjson(self):
        """Test db query for dogs in pet seeker's city."""

        with self.client as c:
            with c.session_transaction() as session:
                session['user_city'] = "San Francisco"

        result = self.client.get('/petmap.json?ani_type=dog')
        self.assertEquals(200, result.status_code)
        self.assertIn("94121", result.data)

    def test_display_pets(self):
        """Test db query for cats in pet seeker's city."""

        result = self.client.get('/display_pets/cat')
        self.assertEquals(200, result.status_code)
        self.assertIn("Heathcliff", result.data)

    def test_add_message(self):
        """Test adding messages to connection request."""

        result = self.client.post('/add_message',
                                  data={"request_id": 1,
                                        "message": "Snoopy is cool!"},
                                  follow_redirects=True)

        self.assertEquals(200, result.status_code)
        self.assertIn("success", result.data)

    def test_member_dashboard(self):
        """Test member dashboard displays."""

        result = self.client.get('/member')
        self.assertEquals(200, result.status_code)
        self.assertIn("Charlie", result.data)

    def test_connect_request(self):
        """Test to see connection request displays all information."""

        result = self.client.get('/connect_request/1')
        self.assertEquals(200, result.status_code)
        self.assertIn("Snoopy", result.data)

    def test_send_connection_request(self):
        """Test sending connection request saves to db."""

        with self.client as c:
            with c.session_transaction() as session:
                session['user_id'] = 2

        result = self.client.post('/connect',
                                  data={"pet_id": 1,
                                        "owner_id": 1,
                                        "connect_message": "Snoopy is too cute!"},
                                  follow_redirects=True)

        self.assertEquals(200, result.status_code)
        self.assertIn("success", result.data)

    def test_change_connect_status(self):
        """Test change status inserts into db."""

        result = self.client.post('/change_connect_status',
                                  data={"request_id": 1,
                                        "connection_status": "Pending Review"},
                                  follow_redirects=True)

        self.assertEquals(200, result.status_code)
        self.assertIn("success", result.data)

    def test_pet_search(self):
        """Test pet search route renders page with member logged in."""

        with self.client as c:
                with c.session_transaction() as session:
                    session['user_id'] = 2

        result = self.client.get('/pet_search')
        self.assertEquals(200, result.status_code)
        self.assertIn("Linus", result.data)

    def test_search_map(self):
        """Test variables are sent to google maps"""
        with self.client as c:
                with c.session_transaction() as session:
                    session['user_id'] = 2
                    session['user_city'] = "San Francisco"

        result = self.client.get('/search_map/dog')
        self.assertEquals(200, result.status_code)
        self.assertIn("San Francisco", result.data)
        self.assertIn("dog", result.data)



# def load_tests(loader, tests, ignore):
#     """Also run our doctests and file-based doctests.

#     This function name, ``load_tests``, is required.
#     """

#     tests.addTests(doctest.DocTestSuite(server))
#     return tests

if __name__ == "__main__":
    unittest.main()

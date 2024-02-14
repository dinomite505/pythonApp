import unittest
# current flask app and generates URLs for application routes dynamically
from flask import current_app, url_for
# creates and configures the Flask app
from app import create_app

# grouping test methods
class TestRoutes(unittest.TestCase):
    def setUp(self):
        # app used for testing
        self.app = create_app()
        # context
        self.app_context = self.app.app_context()
        # makes app and its config available during testing
        self.app_context.push()
    # clean up resources created by setUp method
    def tearDown(self):
        self.app_context.pop()

    def test_index_route(self):
        # creates a test client for the Flask app
        with self.app.test_client() as client:
            response = client.get(url_for("main.index"))
            # checks http status code 
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"FlaskApp with CodePipeline", response.data)

""" api test """
from unittest import TestCase
from api import app


class TestApi(TestCase):
    """test api class"""

    def test_index(self):
        """test home  status 200"""
        tester = app.test_client(self)
        response = tester.get("/")
        status = response.status_code
        self.assertEqual(status, 200)

    def test_response_error(self):
        """test page return error if isbn is  not found"""
        tester = app.test_client(self)
        response = tester.get("/api/v1/book-details/?isbn=1")
        self.assertTrue("error" in response.data)

    def test_response_good(self):
        """test page return json data if isbn is found"""
        tester = app.test_client(self)
        response = tester.get("/api/v1/book-details/?isbn=9781565926219")
        self.assertTrue("isbn" in response.data)

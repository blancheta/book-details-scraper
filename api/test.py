""" api test """
from unittest import TestCase
from api import app


class TestApi(TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status = response.status_code
        self.assertEqual(status, 200)

    def test_isbn_no_found_good(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/book-details/?isbn=1")
        self.assertTrue("error" in response.data)

    def test_isbn_found_good(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/book-details/?isbn=9781565926219")
        self.assertTrue("isbn" in response.data)

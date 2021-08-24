""" api test """
from unittest import TestCase
from api import app


class TestApi(TestCase):

    # test home  status 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        status = response.status_code
        self.assertEqual(status, 200)

    # test page return error if isbn is  not found
    def test_isbn_no_found_response(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/book-details/?isbn=1")
        self.assertTrue("error" in response.data)

    # test page return json data if isbn is found
    def test_isbn_details_response(self):
        tester = app.test_client(self)
        response = tester.get("/api/v1/book-details/?isbn=9781565926219")
        self.assertTrue("isbn" in response.data)

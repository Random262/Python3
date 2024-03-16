import unittest
from m2 import app, RegistrationForm
import json


class TestRegistrationForm(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_registration(self):
        data = {
            "email": "alex@gmail.com",
            "phone1": "9157777777",
            "phone2": "9167777777",
            "name": "Alex",
            "address": "Lenina,15",
            "index": "610000",
            "comment": "Hi"
        }
        data = json.dumps(data)
        response = self.app.post("/registration", data, content_type="application/json")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

import unittest
import requests


class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:5000/registration'

    def test_valid_data(self):
        data = {
            'email': 'test@mail.ru',
            'phone1': 9152458878,
            'phone2': 9164525589,
            'name': 'Alex',
            'address': 'Lenina15',
            'index': 610000
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_email(self):
        data = {
            'email': 'invalidtestmail.ru',
            'phone1': 9152458878,
            'phone2': 9164525589,
            'name': 'Alex',
            'address': 'Lenina15',
            'index': 610000
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone1(self):
        data = {
            'email': 'test@mail.ru',
            'phone1': 915,
            'phone2': 9164525589,
            'name': 'Alex',
            'address': 'Lenina15',
            'index': 610000
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_phone2(self):
        data = {
            'email': 'test@mail.ru',
            'phone1': 9152458878,
            'phone2': -5,
            'name': 'Alex',
            'address': 'Lenina15',
            'index': 610000
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_name(self):
        data = {
            'email': 'test@mail.ru',
            'phone1': 9152458878,
            'phone2': 9164525589,
            'name': '',
            'address': 'Lenina15',
            'index': 610000
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_address(self):
        data = {
            'email': 'test@mail.ru',
            'phone1': 9152458878,
            'phone2': 9164525589,
            'name': 'Alex',
            'address': '',
            'index': 610000
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_invalid_index(self):
        data = {
            'email': 'test@mail.ru',
            'phone1': 9152458878,
            'phone2': 9164525589,
            'name': 'Alex',
            'address': 'Lenina15',
            'index': 'Yes'
        }
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()

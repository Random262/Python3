import unittest
import requests



class TestRegistrationForm(unittest.TestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:5000/run'

    def test_valid_data(self):
        data = {
            'code': 'print(5)',
            'timeout': 5}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 200)

    def test_timeout(self):
        data = {
            'code': 'import time\nprint("Start")\ntime.sleep(3)\nprint("End")',
            'timeout': 2}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Превышено время работы программы', response.text)

    def test_incorrect_timeout(self):
        data = {
            'code': 'import time\nprint(\'Start\')\ntime.sleep(3)\nprint(\'End\')',
            'timeout': 31}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Неправильный ввод', response.text)

    def test_empty_code(self):
        data = {
            'code': '',
            'timeout': 5}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Неправильный ввод', response.text)

    def test_incorrect_code(self):
        data = {
            'code': 'import tim',
            'timeout': 5}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)

    def test_shell_true_code(self):
        data = {
            'code': 'print(5); echo hacked',
            'timeout': 5}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('SyntaxError', response.text)

    def test_io_error(self):
        data = {
            'code': 'import subprocess; subprocess.run(["./echo hacked"])',
            'timeout': 5}
        response = requests.post(self.url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('BlockingIOError', response.text)


if __name__ == '__main__':
    unittest.main()

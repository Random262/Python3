import unittest
from app.m3 import app, storage

class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        storage.update({
            2022: [300, {10: [200, {15: 100, 14: 100}], 11: [100, {15: 100}]}],
            2024: [250, {12: [250, {10: 100, 14: 150}]}]
        })

    def tearDown(self):
        storage.clear()

    def test_add_expense(self):
        response = self.app.get('/add/20230505/250')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(storage[2023][0], 250)

    def test_add_more_expense(self):
        response = self.app.get('/add/20250505/450')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(storage[2025][0], 450)

    def test_calculate_2022year(self):
        response = self.app.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'In the 2022 year spent 300', response.data)

    def test_calculate_2024year(self):
        response = self.app.get('/calculate/2024')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'In the 2024 year spent 250', response.data)

    def test_calculate_month(self):
        response = self.app.get('/calculate/2022/10')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'In 10 month spent 200', response.data)

    def test_calculate_more_month(self):
        response = self.app.get('/calculate/2024/12')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'In 12 month spent 250', response.data)

    def test_invalid_date_format(self):
        with self.assertRaises(TypeError):
            response = self.app.get('/add/2022aa15/100')

    def test_empty_storage(self):
        storage.clear()
        response = self.app.get('/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Data for 2022 year not entered', response.data)

if __name__ == '__main__':
    unittest.main()
import unittest
import datetime

from app.m4 import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Vladimir", 1999, "Lenina, 15")

    def test_get_age(self):
        self.assertEqual(self.person.get_age(), datetime.datetime.now().year - 1999)

    def test_get_name(self):
        self.assertEqual(self.person.get_name(), "Vladimir")

    def test_set_name(self):
        self.person.set_name("Vladislav")
        self.assertEqual(self.person.get_name(), "Vladislav")

    def test_set_address(self):
        self.person.set_address("Mira, 15")
        self.assertEqual(self.person.get_address(), "Mira, 15")

    def test_get_address(self):
        self.assertEqual(self.person.get_address(), "Lenina, 15")

    def test_is_homeless(self):
        self.assertFalse(self.person.is_homeless())


if __name__ == '__main__':
    unittest.main()

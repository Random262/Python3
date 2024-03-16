import unittest

from app.m2 import decrypt

class TestDecrypt(unittest.TestCase):

    def test_no_dots(self):
        with self.subTest():
            self.assertEqual(decrypt(''), '')

        with self.subTest():
            self.assertEqual(decrypt('абра'), 'абра')

    def test_one_dot(self):
        with self.subTest():
            self.assertEqual(decrypt('абра-кадабра.'), 'абра-кадабра')

        with self.subTest():
            self.assertEqual(decrypt('.'), '')

    def test_two_dots(self):
        with self.subTest():
            self.assertEqual(decrypt('абраа..-кадабра'), 'абра-кадабра')

        with self.subTest():
            self.assertEqual(decrypt('абра--..кадабра'), 'абра-кадабра')


    def test_more_than_two_dots(self):
        with self.subTest():
            self.assertEqual(decrypt('абраа..-.кадабра'), 'абра-кадабра')

        with self.subTest():
            self.assertEqual(decrypt('абрау...-кадабра'), 'абра-кадабра')

        with self.subTest():
            self.assertEqual(decrypt('абра........'), '')

        with self.subTest():
            self.assertEqual(decrypt('абр......a.'), 'a')

        with self.subTest():
            self.assertEqual(decrypt('1..2.3'), '23')

        with self.subTest():
            self.assertEqual(decrypt('1.......................'), '')


if __name__ == '__main__':
    unittest.main()

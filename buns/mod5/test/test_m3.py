from app.m3 import BlockErrors
import unittest


class TestBlockError(unittest.TestCase):
    def test_ignore(self):
        with BlockErrors({ZeroDivisionError, TypeError}):
            a = 1 / 0
        print('Выполнено без ошибок')

    def test_raise(self):
        with self.assertRaises(TypeError):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'
        print('Выполнено без ошибок')

    def test_block(self):
        with BlockErrors({TypeError}):
            with BlockErrors({ZeroDivisionError}):
                a = 1 / '0'
            print('Внутренний блок: выполнено без ошибок')
        print('Внешний блок: выполнено без ошибок')

    def test_ignore_child(self):
        with BlockErrors({Exception}):
            a = 1 / '0'
        print('Выполнено без ошибок')

    def fail_test(self):
        try:
            with BlockErrors({ZeroDivisionError}):
                a = 1 / 0
        except:
            self.fail()


if __name__ == '__main__':
    unittest.main()

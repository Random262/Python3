import unittest
import sys
import io
from app.m4 import Redirect


class TestRedirect(unittest.TestCase):
    def test_stdout(self):
        stdout_stream = io.StringIO()
        with Redirect(stdout=stdout_stream):
            print('Hello stdout')
        self.assertEqual(stdout_stream.getvalue(), 'Hello stdout\n')

    def test_stderr(self):
        stderr_stream = io.StringIO()
        with Redirect(stderr=stderr_stream):
            sys.stderr.write('Hello stderr')
        self.assertEqual(stderr_stream.getvalue(), 'Hello stderr')

    def test_out_err(self):
        stdout_stream = io.StringIO()
        stderr_stream = io.StringIO()
        with Redirect(stdout=stdout_stream, stderr=stderr_stream):
            print('Hello stdout')
            sys.stderr.write('Hello stderr')
        self.assertEqual(stdout_stream.getvalue(), 'Hello stdout\n')
        self.assertEqual(stderr_stream.getvalue(), 'Hello stderr')


if __name__ == '__main__':
    unittest.main()
from unittest.mock import patch
from unittest import TestCase
from unittest.mock import call
import unittest

from crypto import main

class Test(TestCase):

    @patch('crypto._input', side_effect=['aaaa', 'bbbb', 'A', ''])
    @patch('crypto._print', create=True)
    def test_something(self, _input, _print):
        main()
        _input.assert_has_calls([
          call('nnnn'),
          call('oooo'),
          call('Only lowercase characters are supported'),
          call('end')
        ])


if __name__ == '__main__':
    unittest.main()
    Mock()

from unittest.mock import patch
from unittest import TestCase
from unittest.mock import call
import unittest

from text_analyzer import main

class Test(TestCase):

    @patch('text_analyzer._input', side_effect=['Hello pretty world', 's'])
    @patch('text_analyzer._print', create=True)
    def test_simple(self, _print, _input ):
        main()
        _input.assert_has_calls([
          call('Please enter some text here: '),
          call('Please choose (s)imple (h)euristic: ')
        ])

        _print.assert_has_calls([
          call('The text contains 3 words:'),
          call('2 word(s) with 5 letters'),
          call('1 word(s) with 6 letters'),
        ])

if __name__ == '__main__':
    unittest.main()
    Mock()

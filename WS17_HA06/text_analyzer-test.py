from unittest.mock import patch
from unittest import TestCase
from unittest.mock import call
import unittest

from text_analyzer import main

class Test(TestCase):

    @patch('text_analyzer._input', side_effect=['Hello, pretty world!', 's', 'English'])
    @patch('text_analyzer._print', create=True)
    def test_simple(self, _print, _input ):
        main()
        _input.assert_has_calls([
          call('Please enter some text here: '),
          call('Please choose (s)imple (h)euristic: '),
          call('Language: ')
        ])

        _print.assert_has_calls([
          call('The text contains 3 words:'),
          call('3 word(s) with 6 letters'),
          call('Average word length is 6.0.')
        ])

    @patch('text_analyzer._input', side_effect=['Hello, pretty world!', 'h', 'English'])
    @patch('text_analyzer._print', create=True)
    def test_heuristic(self, _print, _input ):
        main()
        _input.assert_has_calls([
          call('Please enter some text here: '),
          call('Please choose (s)imple (h)euristic: '),
          call('Language: ')
        ])

        _print.assert_has_calls([
          call('The text contains 3 words:'),
          call('2 word(s) with 5 letters'),
          call('1 word(s) with 6 letters'),
          call('Average word length is 5.333333333333333.')
        ])

    @patch('text_analyzer._input', side_effect=['Hello, pretty world!', 'n', 'English'])
    @patch('text_analyzer._print', create=True)
    def test_nltk(self, _print, _input ):
        main()
        _input.assert_has_calls([
          call('Please enter some text here: '),
          call('Please choose (s)imple (h)euristic: '),
          call('Language: ')
        ])

        _print.assert_has_calls([
          call('The text contains 5 words:'),
          call('2 word(s) with 1 letters'),
          call('2 word(s) with 5 letters'),
          call('1 word(s) with 6 letters'),
          call('Average word length is 3.6.')
        ])

    # test invalid user input
    @patch('text_analyzer._input', side_effect=['Hello, pretty world!', '', 'English'])
    @patch('text_analyzer._print', create=True)
    def test_nomode(self, _print, _input ):
        main()
        _input.assert_has_calls([
          call('Please enter some text here: '),
          call('Please choose (s)imple (h)euristic: '),
          call('Language: ')
        ])

        _print.assert_has_calls([
          call('Mode not supported: ""')
        ])

    # test invalid user input
    @patch('text_analyzer._input', side_effect=['Hello, pretty world!', 'n', 'Hermann'])
    @patch('text_analyzer._print', create=True)
    def test_badlang(self, _print, _input ):
        main()
        _input.assert_has_calls([
          call('Please enter some text here: '),
          call('Please choose (s)imple (h)euristic: '),
          call('Language: ')
        ])

        _print.assert_has_calls([
          call('Language not found: "Hermann". Falling back to "English"')
        ])

if __name__ == '__main__':
    unittest.main()
    Mock()

from unittest.mock import patch
from unittest import TestCase
from unittest.mock import call
import unittest

from myweek import main

class Test(TestCase):

    @patch('myweek._input', side_effect=['1000', '100'])
    @patch('myweek._print', create=True)
    def test_something(self, _input, _print):
        main()
        _input.assert_has_calls([
          call('Updating. Do not turn off your computer.'),
          call('0%'),
          call('10%'),
          call('20%'),
          call('30%'),
          call('40%'),
          call('50%'),
          call('60%'),
          call('70%'),
          call('80%'),
          call('90%'),
          call('100%'),
          call('DONE')
        ])

    @patch('myweek._input', side_effect=['10', '4'])
    @patch('myweek._print', create=True)
    def test_something(self, _input, _print):
        main()
        _input.assert_has_calls([
          call('Updating. Do not turn off your computer.'),
          call('0%'),
          call('40%'),
          call('80%'),
          call('100%'),
          call('DONE')
        ])

    @patch('myweek._input', side_effect=['A', '12', '7'])
    @patch('myweek._print', create=True)
    def test_something(self, _input, _print):
        main()
        _input.assert_has_calls([
          call('Updating. Do not turn off your computer.'),
          call('0%'),
          call('58%'),
          call('100%'),
          call('DONE')
        ])


if __name__ == '__main__':
    unittest.main()
    Mock()

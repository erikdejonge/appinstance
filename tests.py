# coding=utf-8
"""
appinstance
erik@a8.nl (04-03-15)
license: GNU-GPL2
"""

import unittest
from appinstance import AppInstance, AppInstanceRunning


def more_then_one():
    """
    more_then_one
    """
    with AppInstance("arg1", verbose=False):
        with AppInstance("arg1", verbose=False):
            pass  # error here


def more_then_one_different_args():
    """
    more_then_one
    """
    with AppInstance("arg1", verbose=False):
        with AppInstance("arg2", verbose=False):
            pass  # no error here


class ExceptionTest(unittest.TestCase):

    def test_assert_raises(self):
        """
        test_assert_raises
        """
        self.assertRaises(AppInstanceRunning, more_then_one)

    def test_assert_not_raises(self):
        """
        test_assert_not_raises
        """
        more_then_one_different_args()


def main():
    """
    main
    """
    unittest.main()


if __name__ == "__main__":
    main()

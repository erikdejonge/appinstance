# coding=utf-8
"""
appinstance
Active8 (04-03-15)
license: GNU-GPL2
"""

from unittester import *

from appinstance import AppInstance, AppInstanceRunning


def more_then_one():
    """
    more_then_one
    """
    with AppInstance("arg1"):
        with AppInstance("arg1"):
            pass  # error here


def more_then_one_different_args():
    """
    more_then_one
    """
    with AppInstance("arg1"):
        with AppInstance("arg2"):
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
    unit_test_main(globals())


if __name__ == "__main__":
    main()

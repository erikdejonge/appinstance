# coding=utf-8
"""
sample program 1
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from appinstance import AppInstance, AppInstanceRunning

import time


def main():
    """
    main
    """
    try:
        with AppInstance("arg1", True):
            print("sleep for 5 sec")
            time.sleep(2)
    except AppInstanceRunning:
        print("already running")


if __name__ == "__main__":
    main()

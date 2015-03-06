# coding=utf-8
"""
appinstance
Active8 (04-03-15)
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

import time
from appinstance import AppInstance, AppInstanceRunning


def main():
    """
    main
    """
    try:
        with AppInstance("arg2", True):
            print("sleep for 2 sec")
            time.sleep(2)
    except AppInstanceRunning:
        print("already running")


if __name__ == "__main__":
    main()

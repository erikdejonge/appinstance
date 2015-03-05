# coding=utf-8
"""
sample program 1
"""
from appinstance import AppInstance, AppInstanceRunning

import time


def main():
    """
    main
    """
    try:
        with AppInstance("arg1", True):
            print "sleep for 5 sec"
            time.sleep(2)
    except AppInstanceRunning:
        print "already running"


if __name__ == "__main__":
    main()

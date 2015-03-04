# coding=utf-8
"""
appinstance
Active8 (04-03-15)
"""
import time
from appinstance import AppInstance, AppInstanceRunning


def main():
    """
    main
    """
    try:
        with AppInstance("arg2", True):
            print "sleep for 2 sec"
            time.sleep(2)
    except AppInstanceRunning:
        print "already running"
        


if __name__ == "__main__":
    main()

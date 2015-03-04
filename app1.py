
"""
sample program 1
"""
from appinstance import AppInstance, AppInstanceRunning

import time


def main():
    """
    main
    """
    with AppInstance("app1", True):
        print "sleep for minute"
        time.sleep(60)


if __name__ == "__main__":
    main()

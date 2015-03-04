# coding=utf-8
"""
appinstance
Active8 (04-03-15)
"""
from appinstance import AppInstance, AppInstanceRunning


def main():
    """
    main
    """
    with AppInstance("app2", True):
        print "sleep for minute"
        time.sleep(60)


if __name__ == "__main__":
    main()

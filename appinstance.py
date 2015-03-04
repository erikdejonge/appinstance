# coding=utf-8
"""

# appinstance
Check if an app with the same name is running, supports parameters.
Erik de Jonge
erik@a8.nl
license: gpl2
"""

import os
import psutil
import hashlib
from os.path import basename, join, expanduser, exists


import __main__ as main


class AppInstanceRunning(AssertionError):
    """
    AppInstanceRunning
    """
    pass


class AppInstance(object):
    """
    Lockfile
    """
    def __init__(self, arguments=None, verbose=False):
        """
        @type arguments: str, unicode
        @type verbose: bool
        @return: None
        """
        self.verbose = verbose
        self.arguments = arguments
        self.name = main.__file__.split(".")[0]

        if arguments is None:
            self.lockfile = join(expanduser("~"), "." + self.name + ".pid")
        else:
            uname = str(basename(self.name)) + "-" + str(arguments)
            lfname = hashlib.md5(uname).hexdigest()
            self.lockfile = join(expanduser("~"), "." + self.name + "_" + lfname + ".pid")

    def __exit__(self, t, value, traceback):
        """
        @type t: str, unicode
        @type value: str, unicode
        @type traceback: str, unicode
        @return: None
        """
        if exists(self.lockfile):
            if int(open(self.lockfile).read()) == os.getpid():
                os.remove(self.lockfile)

    def __enter__(self):
        """
        __enter__
        """
        running = False

        if exists(self.lockfile):
            pid = int(open(self.lockfile).read().strip())
            cmdline = None

            for p in psutil.process_iter():
                if p.pid == pid:
                    cmdline = " ".join(p.as_dict()["cmdline"])

                    if self.name in str(cmdline):
                        running = True

            if running is False:
                os.remove(self.lockfile)

            if self.verbose is True:
                if running is True:
                    print "\033[91mAnother instance found:", pid, "\033[0m"

        if not running:
            fh = open(self.lockfile, "w")
            fh.write(str(os.getpid()))
            fh.close()

            if self.verbose is True:
                print "\033[32mOk:", self.name, self.lockfile, str(os.getpid()) + "\033[0m"
        else:
            if self.verbose:
                print "\033[32mError:", self.name, self.lockfile, str(os.getpid()) + "\033[0m"
            raise AppInstanceRunning(self.lockfile)

        return running

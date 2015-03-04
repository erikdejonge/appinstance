
"""
# appinstance
Check if an app with the same name is running, supports parameters.

Erik de Jonge
erik@a8.nl
license: gpl2
"""

import psutil
from os.path import basename, join, expanduser


class AppInstanceRunning(AssertionError):
    """
    @type AssertionError: str, unicode
    @return: None
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
        name = basename(__file__).split(".")[0]

        if arguments is None:
            self.lockfile = join(expanduser("~"), "." + name + ".pid")
        else:
            lfname = hashlib.md5(basename(__file__) + arguments).hexdigest()
            self.lockfile = join(expanduser("~"), "." + name + "_" + lfname + ".pid")

    def __exit__(self, t, value, traceback):
        """
        @type t: str, unicode
        @type value: str, unicode
        @type traceback: str, unicode
        @return: None
        """
        print "\033[92m", t, "\033[0m"
        print "\033[93m", value, "\033[0m"
        print "\033[94m", traceback, "\033[0m"
        if os.path.exists(self.lockfile):
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

                    if __file__ in str(cmdline):
                        running = True

            if running is False:
                os.remove(self.lockfile)

            if self.verbose is True and cmdline is not None and running is False:
                print "\033[91mAnother type proc found:", pid, "\033[0m"

            if self.verbose is True:
                if running is True:
                    print "\033[91mAnother instance found:", pid, "\033[0m"

        if not running:
            fh = open(self.lockfile, "w")
            fh.write(str(os.getpid()))
            fh.close()

            if self.verbose is True:
                print "\033[32m" + self.lockfile, str(os.getpid()) + "\033[0m"
        else:
            raise AppInstanceRunning(self.lockfile)

        return running

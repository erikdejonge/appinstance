# appinstance
Check if an app with the same name is running, supports parameters.

###intention
In cronjobs to detect if a program with the same arguments is already running

###usage

```python
from appinstance import AppInstance, AppInstanceRunning
import time

try:
    # use Appinstance context manager, "arg1" is a good place for commandline variables.
    with AppInstance("arg1", True):
        print "sleep for 2 sec"
        time.sleep(2)
except AppInstanceRunning:
    print "already running"
```
#! /usr/bin/env python
from subprocess import call
import time
while(True):
    call(['espeak "Hello Lynn" 2>/dev/null'], shell=True)
    time.sleep(10)
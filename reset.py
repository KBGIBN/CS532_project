#!/usr/bin/python
import os
import sys
import shutil

# Get directory name
mydir= './runs/detect/exp'

try:
    shutil.rmtree(mydir)
except OSError as e:
    print("Error: %s - %s." % (e.filename, e.strerror))
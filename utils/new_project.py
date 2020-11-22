#!/usr/bin/env python
import glob
import os
import shutil
import argparse
import fileinput

## Main Script
parser = argparse.ArgumentParser(description='creates new project')
parser.add_argument('platform', help='hardware platform. ie patch, field, etc.')
parser.add_argument('name', help='name of new project')
args = parser.parse_args()
platform = args.platform
name = args.name
src = '../' + platform + '/Template'
dest = '../' + platform + '/' + name

# Get some helper variables for directory/file names.
srcAbs = os.path.abspath(src)
srcBase = os.path.basename(srcAbs)
destAbs = os.path.abspath(dest)
destBase = os.path.basename(destAbs)

# First check if src is valid directory.
if os.path.isdir(srcAbs):
    # Then make a copy of the folder renaming it to be the same
    shutil.copytree(srcAbs, destAbs)
    # Go through and rename all the files first.
    found = glob.glob(destAbs+'/*' + srcBase + '*')
    for f in found:
        s = os.path.abspath(f)
        d = os.path.abspath(f.replace(srcBase, destBase))
        os.rename(s, d)
    allFiles = glob.glob(destAbs + '/*')
    for f in allFiles:
        if not os.path.isdir(f) and os.path.exists(f):
            with fileinput.FileInput(f, inplace=True) as modFile:
                for line in modFile:
                    print(line.replace(srcBase, destBase), end='')


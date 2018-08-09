#!/usr/bin/python

from __future__ import print_function

import argparse
import sys


HELP = """
Usage: $0 [flag [flag]]

Flags:
  --major  - include the major version substring
  --minor  - include the minor version substring
  --micro  - include the micro/bugfix version substring

One or more flags can be passed in, and the same flag passed in more than once
has no further effect.
If no flags are passed in, the entire original version string is printed.
"""

# Parse the arguments to the script
parser = argparse.ArgumentParser(description='Get the version of Python')
parser.add_argument('--major', dest='major', action='store_true', default=False)
parser.add_argument('--minor', dest='minor', action='store_true', default=False)
parser.add_argument('--micro', dest='micro', action='store_true', default=False)

args = parser.parse_args()

# Build the version tuple
version_tuple = tuple()
if args.major:
    version_tuple += (sys.version_info[0],)
if args.minor:
    version_tuple += (sys.version_info[1],)
if args.micro:
    version_tuple += (sys.version_info[2],)
if not any([args.major, args.minor, args.micro]):
    version_tuple = tuple(version_part for version_part in sys.version_info)

print('.'.join([str(el) for el in version_tuple]))

#!/usr/local/bin/python

from __future__ import print_function

import sys

from st2common.runners.base_action import Action


def get_version_string(major=False, minor=False, micro=False):
    """
    Return all or part of the Python version string.

    If all parameters are False-y, returns the entire, unmangled Python version
    string

    Parameters
    ----------
    major : boolean
        If True, includes the major version in the returned Python version
        string
    minor : boolean
        If True, includes the minor version in the returned Python version
        string
    micro : boolean
        If True, includes the micro/bugfix version in the returned Python
        version string

    Returns
    -------
    str
        The constructed version string
    """
    version_tuple = tuple()
    if major:
        version_tuple += (sys.version_info[0],)
    if minor:
        version_tuple += (sys.version_info[1],)
    if micro:
        version_tuple += (sys.version_info[2],)
    if not any([major, minor, micro]):
        version_tuple = tuple(version_part for version_part in sys.version_info)

    return '.'.join([str(el) for el in version_tuple])


class GetVersionStringAction(Action):
    """
    StackStorm Action for the python-script runner that wraps the
    get_version_string function.

    Only accepts and passes the major and minor parameters.
    """
    def run(self, major, minor):
        return {
            "version": get_version_string(major=major, minor=minor),
            "major": get_version_string(major=True),
            "minor": get_version_string(minor=True),
            "micro": get_version_string(micro=True),
        }

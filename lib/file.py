"""
[fTerm] file.py

This module defines all of the standard file operations of fTerm.
"""

# NOTE: this is extraneous
# pylint: disable-msg=C0103


synonyms = {
    "display":"read",
    "write":"edit",
    "compose":"edit",
    "revise":"edit",
    "append":"addline",
    "removeline":"removeline",
    }


def read(*files):
    """Read a file."""
    return 'cat %s;' % tuple(files)

def edit(*files):
    """Edit a file."""
    return 'nano %s;' * len(files) % tuple(files)

def addline(filename, line):
    """Append *line* to *filename*."""
    return 'echo %s >> %s;' % (line, filename)

def removeline(filename, line):
    """Remove *line* from file *filename*."""

    data = open(filename.replace("\\", ""), "r").readlines()

    del data[int(line)]

    open(filename.replace("\\", ""), "w").writelines(data)

    return ":;"
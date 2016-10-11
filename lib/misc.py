"""
[fTerm] misc.py

This module defines some miscellaneous commands for fTerm.
"""

# NOTE: this is extraneous
# pylint: disable=C0103,C0303

synonyms = {
    "space":"size",
    
    "exec":"run",
    "execute":"run",
    "evaluate":"run",

    "end":"kill",

    "man":"rtfm",
    
    "fterm-edition":"fterm_version",
    "version":"fterm_version",
    }

def size(*files):
    """Return the size of a file in human-readable format."""
    return "du -sh %s;" * len(files) % files

def run(*files):
    """A universal run function."""

    # filter filename to appropriate command
    command = {"py" : "python %s;", "rb" : "ruby %s;", "sh" : "sh %s;", "pl" : "perl %s;"}

    # run the files
    return ''.join(["echo %s:;" % (x)
                    + command.setdefault(x.split(".")[1]
                                         , "echo '[f-i] Filetype %s not recognized';")
                    % (x) for x in files])

def kill(*processes, **keywords):
    """Kill the process with name *processname*."""
    adj_prefix = ""
    if ["force"] in keywords.values():
        adj_prefix += "-9"    
    return "pkill %s %s;" * len(processes) % ((adj_prefix,)* len(processes), tuple(processes))

def rtfm(*manpages):
    """Fun shortcut to man."""
    return "man %s;" % " ".join(manpages)

def fterm_version():
    """Return the current version of fTerm."""
    return "echo {VERSION};"

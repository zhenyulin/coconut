#!/usr/bin/python

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# INFO:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
Author: Evan Hubinger
Date Created: 2015
Description: Coconut Utilities.
"""

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# IMPORTS:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from __future__ import with_statement, print_function, absolute_import, unicode_literals, division

from .root import *

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# UTILITIES:
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def openfile(filename, opentype="r+b"):
    """Returns An Open File Object."""
    return codecs.open(str(filename), str(opentype), encoding=encoding)

def writefile(openedfile, writer):
    """Sets The Contents Of A File."""
    openedfile.seek(0)
    openedfile.truncate()
    openedfile.write(writer)

def readfile(openedfile):
    """Reads The Contents Of A File."""
    openedfile.seek(0)
    return str(openedfile.read())

class terminal(object):
    """Wraps Base Terminal Commands To Create A Fake Console."""
    colors = {
        "end" : "\033[0m",
        "bold" : "\033[1m",
        "blink" : "\033[5m",
        "black" : "\033[30m",
        "red" : "\033[31m",
        "green" : "\033[32m",
        "yellow" : "\033[33m",
        "blue" : "\033[34m",
        "magenta" : "\033[35m",
        "cyan" : "\033[36m",
        "white" : "\033[37m",
        "blackhighlight" : "\033[40m",
        "redhighlight" : "\033[41m",
        "greenhighlight" : "\033[42m",
        "yellowhighlight" : "\033[43m",
        "bluehighlight" : "\033[44m",
        "magentahighlight" : "\033[45m",
        "cyanhighlight" : "\033[46m",
        "whitehighlight" : "\033[47m",
        "pink" : "\033[95m",
        "purple" : "\033[94m",
        "lightgreen" : "\033[92m",
        "lightyellow" : "\033[93m",
        "lightred" : "\033[91m"
        }

    def __init__(self, on=True, color=None):
        """Base Constructure For The Terminal Wrapper."""
        self.clear()
        self.on = on
        self.color = color
    def clear(self):
        """Clears The History."""
        self.history = []
    def addcolor(self, inputstring, color):
        """Adds The Specified Colors To The String."""
        if islist(color):
            out = ""
            for item in color:
                out += self.colors[str(item)]
        else:
            out = self.colors[str(color)]
        return out+str(inputstring)+self.colors["end"]
    def delcolor(self, inputstring):
        """Removes Recognized Colors From A String."""
        inputstring = str(inputstring)
        for x in self.colors:
            inputstring = inputstring.replace(x, "")
        return inputstring
    def colorwrap(self, message):
        """Wraps A Message In The Color."""
        message = str(message)
        if self.color in self.colors:
            message = self.addcolor(message, self.color)
        return message
    def display(self, *messages):
        """Prints A Message."""
        if self.doshow:
            message = " ".join(messages)
            for line in message.splitlines():
                print(self.colorwrap(line))
                self.history.append(line)
    def history(self):
        """Retreives All Lines In The History."""
        return self.history[:]

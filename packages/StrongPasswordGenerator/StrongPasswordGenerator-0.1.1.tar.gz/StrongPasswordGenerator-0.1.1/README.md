Description
===========
strongPasswordGenerator can be used as a command line utility to generate passwords or as a python module.

You determine the complexity of the password, and the password is considered randomly as safe as in your trust to os.urandom().
https://docs.python.org/3/library/os.html#os.urandom.

Installation
============
python setup.py install

Usage
=====

If no options are specified:
* Password length : 15
* Pattern : !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}

usage: strongPasswordGenerator [options]

Preset patterns to be used with -x flag:
1. [a-zA-Z0-9] - abcDEF789
2. [a-f0-9] - Hexadecimal
3. [\.\-] - Morse

~~~~
optional arguments:
-h, --help    show this help message and exit
-x PATTERN    Specifies pattern preset, overrides whitelist
-w WHITELIST  Regex pattern for allowed characters
-b BLACKLIST  Regex pattern for disallowed characters
-v            Verbose mode
-q            Avoid similar characters (1iIl0oO'´\`\|.,), overrides blacklist
-c LENGTH     Password length
~~~~

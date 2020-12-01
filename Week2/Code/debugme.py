#!/bin/env python3

# Author: ph-u
# Script: debugme.py
# Desc: testing %ipdb by creating a bug
# Input: python3 debugme.py
# Output: hault at break point and go into python3 debug mode
# Arguments: 0
# Date: Oct 2019

"""testing %ipdb by creating a bug"""

__appname__="debugme.py"
__author__="ph-u"
__version__="0.0.1"
__license__="None"

def makeabug(x):
    """test"""
	y=x**4
	z=0.
	import ipdb; ipdb.set_trace() ## set up break point in debug mode
	y=y/z
	return y
makeabug(25)

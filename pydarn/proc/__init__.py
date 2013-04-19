# Processing module __init__.py
"""
*******************************
            PROC
*******************************
This subpackage contains various data processing routines for DaViT-py
DEV: functions/modules/classes with a * have not been developed yet

This includes the following function(s):
	gridLib
		library of functions and classes needed 
		for gridding vectors
	gridIo
		library of pygrid I/O functions

*******************************
"""

try: import pygridLib 
except Exception, e: 
    print 'problem importing pydarn.proc.pygridLib: ', e

#import simLib
#from simLib import *
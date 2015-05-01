#!/usr/bin/python3

import sys
from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["os","matplotlib","tkinter"]}
setup( name = "GraphCalc",
	version = "0.1",
	description = "Graphing Calculator in Python",
	options = {"build_exe": build_exe_options},
	executables = [Executable("GraphCalc.py",base=None)])

#!/usr/bin/python3

import sys
from cx_Freeze import setup, Executable
build_exe_options = {"packages": ["os","matplotlib","tkinter","numpy"]}
setup( name = "GraphCalc",
	version = "0.3",
	description = "Graphing Calculator in Python",
	options = {"build_exe": build_exe_options},
	executables = [Executable("src/GraphCalc.py",base=None)])

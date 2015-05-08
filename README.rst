GraphCalc
=========

What is GraphCalc?
------------------
GraphCalc is intended as a replacement for TI graphing calculators.
Right now we are aiming to replicate most of the TI-84 Plus.

How do I use it?
----------------
There are a couple of ways to use Graph Calc:

1. Run GraphCalc.py through Python 3 with matplotlib installed
2. Run a frozen version, availiable through Github_.

Known Issues
------------
- The math evaluator requires an exact relation between two terms; that is 3x will not evaluate but 3*x will
- /points plots on current graph

How do I add a command to GraphCalc?
------------------------------------
1. Add a new python file under src
2. Make sure that any exported functions:
	- Take an argument list
	- Treat the first entry in the argument list as the name of the command
	- Print any output they give nicely
3. Edit src/command.py to import your new files
4. Add an entry to the coms dictionary in src/command.py for your new command that calls the function in your new file
5. Add a new entry in the help dictionary in src/help.py for your command
6. (Optional) Add error checking that calls help.helper with the name of your command as a string argument
7. Submit a pull request to the Github_. or a patch to tookmund@gmail.com

License
-------
GraphCalc, a graphing calculator program
Copyright (C) 2015 Jacob Adams <tookmund@gmail.com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


.. _Github: https://github.com/tookmund/graphcalc/releases



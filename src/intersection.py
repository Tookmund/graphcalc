from graph import genpoints
import help
from numpy import *

helper = {'/intersect':'<equation1> <equation2> <min> <max>: Calculate intersection between two y= equations'}

def intersect(args):
	if len(args) < 4:
		help.helper("intersect")
		return None
	eq1 = args[1]
	eq2 = args[2]
	rg = linspace(int(float(args[3])),int(float(args[4])))
	pts1 = genpoints(eq1,rg,'x')
	pts2 = genpoints(eq2,rg,'x')
	print(pts1)
	print(pts2)
	out = {}
	for x,y in pts1.items():
		if pts2[x] == y:
			out.update({x:y})
	for x in out:
        	print("(%f,%f)\n" % (x,out[x]))	

coms = {'/intersect':intersect}

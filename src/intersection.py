from graph import genpoints
import help
from numpy import *

helper = {'/intersect':'<equation1> <equation2> <min> <max>: Calculate intersection between two y= equations'}

# http://stackoverflow.com/a/3252222
def perp( a ) :
	b = empty_like(a)
	b[0] = -a[1]
	b[1] = a[0]
	return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2

def seg_intersect(a1,a2, b1,b2): 
	da = a2-a1
	db = b2-b1
	dp = a1-b1
	dap = perp(da)
	denom = dot( dap, db)
	num = dot( dap, dp )
	return (num / denom.astype(float))*db + b1

def intersect(args):
	if len(args) < 4:
		help.helper("intersect")
		return None
	eq1 = args[1]
	eq2 = args[2]
	rg = range(int(float(args[3])),int(float(args[4])))
	total = int(float(args[4]))
	pts1x,pts1y = genpoints(eq1,rg,'x')
	pts2x,pts2y = genpoints(eq2,rg,'x')
	pts1begin = array([pts1x[0],pts1y[0]])
	pts1end = array([pts1x[total],pts1y[total]])
	pts2begin = array([pts2x[0],pts2y[0]])
	pts2end = array([pts2x[total],pts2y[total]])
	print(seg_intersect(pts1begin,pts1end,pts2begin,pts2end))

coms = {'/intersect':intersect}

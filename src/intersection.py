from graph import genpoints
import help
import scipy.interpolate as interpolate
import scipy.optimize as optimize
import numpy as np

helper = {'/intersect':'<equation1> <equation2> <min> <max>: Calculate intersection between two y= equations'}
p1=None
p2=None

def pdiff(x):
    return p1(x)-p2(x)

def intersect(args):
    if len(args) < 4:
        help.helper("intersect")
        return None
    eq1 = args[1]
    eq2 = args[2]
    rg = range(int(float(args[3])),int(float(args[4]))) 
    pts1x,pts1y = genpoints(eq1,rg,'x')
    pts2x,pts2y = genpoints(eq2,rg,'x')
    # http://stackoverflow.com/a/8095198
    x1=np.array(pts1x)
    y1=np.array(pts1y)
    x2=np.array(pts2x)
    y2=np.array(pts2y)
    global p1,p2
    p1=interpolate.PiecewisePolynomial(x1,y1[:,np.newaxis])
    p2=interpolate.PiecewisePolynomial(x2,y2[:,np.newaxis])
    xs=np.r_[x1,x2]
    xs.sort()
    x_min=xs.min()
    x_max=xs.max()
    x_mid=xs[:-1]+np.diff(xs)/2
    roots=set()
    for val in x_mid:
        root,infodict,ier,mesg = optimize.fsolve(pdiff,val,full_output=True)
        # ier==1 indicates a root has been found
        if ier==1 and x_min<root<x_max:
            roots.add(root[0])
    roots=list(roots)
    for i in roots:
        print("(%d,%d)" % (i,p1(i)))

coms = {'/intersect':intersect}

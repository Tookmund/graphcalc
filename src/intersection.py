from graph import genpoints
import help

helper = {'/intersect':'<equation1> <equation2> <min> <max>: Calculate intersection between two y= equations'}
def intersect(args):
    if len(args) < 4:
        help.helper("intersect")
        return None
    eq1 = args[1]
    eq2 = args[2]
    rg = range(int(float(args[3])),int(float(args[4])))
    
    pts1x,pts1y = genpoints(eq1,rg,'x')
    pts2x,pts2y = genpoints(eq2,rg,'x')
    out = []
    for x in rg:
        if pts1x[x] == pts2x[x] and pts1y[x] == pts2y[x]:
            out.append((pts1x[x],pts1y[x]))
    for x in out:
        print("%s\n" % (x,))

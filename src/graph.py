import matplotlib.pyplot as plt
from eval import Parser
import vars
import help
parser = Parser()
def setup():
        plt.ion()

helper = {'/graph' : '<y/x> <equation> <min> <max> [figure]: Graph a function. If figure given, graph in the given figure'}

numfig = 1
		
def graph(str):
	if len(str) < 4:
		help.helper("graph")
		return None
	global numfig
	try:
		plt.figure(int(str[5]))
	except:
		plt.figure(numfig)
		numfig += 1

	plt.title(str[2])
	plt.grid()
	start = int(float(str[3]))
	end = int(float(str[4]))
	rg = range(start,end)
	if str[1] == 'x':
		xeq(str[2],rg)
	elif str[1] == 'y':
                yeq(str[2],rg)

coms = {'/graph': graph}
def genpoints(equation,rg,xy):
        inp = []
        out = []
        for x in rg:
                vars.vars[xy] = x
                inp.append(x)
                y = parser.evaluate(equation, vars.vars)
                out.append(y)
        return (inp,out)

def yeq(equation,rg):
	xlist,ylist = genpoints(equation,rg,'x')
	plt.plot(xlist,ylist)

def xeq(equation,rg):
	ylist,xlist = genpoints(equation,rg,'y')
	plt.plot(xlist,ylist)

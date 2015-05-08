import matplotlib.pyplot as plt
from eval import Parser
import vars
import help
parser = Parser()
def setup():
        plt.ion()
	

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

	
def yeq(equation,rg):
	xlist = []
	ylist = []
	for x in rg:
		vars.vars['x'] = x
		xlist.append(x)
		y = parser.evaluate(equation, vars.vars)
		ylist.append(y)
		plt.plot(xlist,ylist)

def xeq(equation,rg):
	xlist = []
	ylist = []
	for y in rg:
		vars.vars['y'] = y
		ylist.append(y)
		x = parser.evaluate(equation, vars.vars)
		xlist.append(x)
	plt.plot(xlist,ylist)

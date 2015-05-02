import matplotlib.pyplot as plt
from eval import Parser
from vars import vars
parser = Parser()
def setup():
        plt.ion()
	

numfig = 1
		
def graph(str):
	if len(str) < 4:
		print("Wrong arguements: "+str(help.help(["","graph"])))
		return None
	global numfig
	plt.figure(numfig)
	rg = range(int(float(str[3])),int(float(str[4])))
	if str[1] == 'x':
		xeq(str[2],rg)
	elif str[1] == 'y':
                yeq(str[2],rg)
        numfig += 1

	
def yeq(equation,rg):
	xlist = []
	ylist = []
	for x in rg:
		vars['x'] = x
		xlist.append(x)
		y = parser.evaluate(equation, vars)
		ylist.append(y)
		plt.plot(xlist,ylist)

def xeq(equation,rg):
	xlist = []
	ylist = []
	for y in rg:
		vars['y'] = y
		ylist.append(y)
		x = parser.evaluate(equation, vars)
		xlist.append(x)
	plt.plot(xlist,ylist)

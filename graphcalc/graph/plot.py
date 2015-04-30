import matplotlib.pyplot as plt
from py_expression_eval import Parser

parser = Parser()

def yeq(equation,rg):
	xlist = []
	ylist = []
	for x in rg:
		xlist.append(x)
		y = parser.evaluate(equation, {'x': x})
		ylist.append(y)
		#print("x: %s y: %s" %(x,y))
	plt.plot(xlist,ylist)
	plt.show()

def xeq(equation,rg):
	xlist = []
	ylist = []
	for y in rg:
		ylist.append(y)
		x = parser.evaluate(equation, {'y': y})
		xlist.append(x)
		#print("x: %s y: %s" %(x,y))
	plt.plot(xlist,ylist)
	plt.show()

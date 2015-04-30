import matplotlib.pyplot as plt

def yeq(equation,range):
	xlist = []
	ylist = []
	for x in range:
		xlist.append(x)
		y = eval(equation)
		ylist.append(y)
	
	plt.plot(xlist,ylist)
	plt.show()

import matplotlib.pyplot as plt
import help

def plot(args):
	if len(args) < 2:
		help.helper("points")
		return None
	xlist = []
	ylist = []
	for x in args[1:]:
		pt = x.split(",")
		xlist.append(pt[0])
		ylist.append(pt[1])
	plt.plot(xlist,ylist,'o')


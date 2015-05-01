import matplotlib.pyplot as plt
from py_expression_eval import Parser
try:
	import threading
except ImportError:
	import dummy_threading as threading

parser = Parser()

class ythread(threading.Thread):
	def __init__(self,eq,rg):
		threading.Thread.__init__(self)
		self.eq = eq
		self.rg = rg
	
	def run(self):
		yeq(self.eq,self.rg)

class xthread(ythread):
	def run(self):
		xeq(self.eq,self.rg)

threads = []
numthreads = 0

def cleanup():
	for x in threads:
		x.join()
		
def graph(str):
	plt.figure(numthreads)
	global threads
	global numthreads
	rg = range(int(float(str[3])),int(float(str[4])))
	if str[1] == 'x':
		thread = xthread(str[2],rg)
	elif str[1] == 'y':
		thread = ythread(str[2],rg)
	else:
		thread = None
	threads.append(thread)
	try:
		threads[numthreads].start()
	except RuntimeError:
		pass

	numthreads += 1
	#print("threading")

	
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

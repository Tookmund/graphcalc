import matplotlib.pyplot as plt
from eval import Parser

parser = Parser()
def setup():
        plt.ion()
	

numfig = 1
		
def graph(str):
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
                xlist.append(x)
                y = parser.evaluate(equation, {'x': x})
                ylist.append(y)
                #print("x: %s y: %s" %(x,y))
        plt.plot(xlist,ylist)
        #plt.show()

def xeq(equation,rg):
        xlist = []
        ylist = []
        for y in rg:
                ylist.append(y)
                x = parser.evaluate(equation, {'y': y})
                xlist.append(x)
                #print("x: %s y: %s" %(x,y))
        plt.plot(xlist,ylist)

import graphcalc.graph as graph
import py_expression_eval as pyee

vars = {}
parser = pyee.Parser()

def set(str):
	vars[str[1]] = str[2]

def get(str):
	return vars[str[1]]
	
def parse(string):
	if string[:1] == '/':
		command(string)
	else:
		ps = parser.evaluate(string,vars)
		print(ps)

coms = {
	'/set': set,
	'/get': get,
	'/graph': graph.graph
}

def command(string):
	str = string.split(" ")
	rt = coms[str[0]](str)
	if not (rt is None):
		print(rt)

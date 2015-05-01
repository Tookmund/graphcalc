import graph
import eval as evalu 
import stats
import pprint
pp = pprint.PrettyPrinter()
vars = {}
parser = evalu.Parser()

def set(str):
	vars[str[1]] = float(str[2])

def get(str):
	try:
		return vars[str[1]]
	except:
		pass
	
def parse(string):
	if string[:1] == '/':
		command(string)

	else:
		try:
			ps = parser.evaluate(string,vars)
			pp.pprint(ps)
		except:
			print("Failed to parse: %s" % (string))	

def helper(extra):
	print("""
Type any expression and it will simplify it to a single number
Ctrl+C to exit
/help : Show this menu
/set (name) (value) : Set variable
/get (name) : Get variable
/graph (y/x) (equation) (min) (max) : Graph a function 
/stats (list) : Calculate statistics
""")

coms = {
	'/help': helper,
	'/set': set,
	'/get': get,
	'/graph': graph.graph,
	'/stats': stats.stats
}

def command(string):
	str = string.split(" ")
	if str[0] in coms:
		rt = coms[str[0]](str)
		if not (rt is None):
			pp.pprint(rt)
	else:
		print("%s is not a vaild command" % str[0])


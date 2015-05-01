import graph
import eval as pyee
import stats
import pprint
pp = pprint.PrettyPrinter()
vars = {}
parser = pyee.Parser()

def set(str):
	vars[str[1]] = str[2]

def get(str):
	return vars[str[1]]
	
def parse(string):
	#print(string.split())
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
/help : Show this menu
/graph : graph a function (y/x) (equation) (min) (max)
/stats : calculate statistics (list)
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
			#print(rt)
	else:
		print("%s is not a vaild command" % str[0])


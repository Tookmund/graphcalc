help = {
'/help' : '[name]: Show usage of command. Without arguments, show all',
'/set' : '<name> <value>: Set variable',
'/get' : '<name>: Get variable',
'/graph' : '<y/x> <equation> <min> <max> [figure]: Graph a function. If figure given, graph in the given figure', 
'/stats' : '<list>: Calculate statistics',
'/perm' : '<total> <pick>: Calculate permuations',
'/combo' : '<total> <pick>: Calulate combinations',
'/sigma' : '<equation> <variable> <start> <end>: Calcuate summation'
}
def helper(st):
	if isinstance(st,str):
		com = '/'+st
		print("""Wrong Arguments: 
%s %s""" % (com,help[com]))
		return None
	try:
		com = '/'+st[1]
		print("%s %s" % (com,help[com]))
	except:
		print("""
Type any expression and it will simplify it to a single number
Ctrl+C to exit
""")
		for x,y in help.items():
			print("%s %s\n" % (x,y))

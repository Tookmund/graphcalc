help = {}
def setuphelp():
        global help
        import graph 
        import stats 
        import comboandperm 
        import vars
        import sigma
        import points
        import intersection
        help = {'/help' : '[name]: Show usage of command. Without arguments, show all'}
        help.update(graph.helper)
        help.update(stats.helper)
        help.update(comboandperm.helper)
        help.update(vars.helper)
        help.update(sigma.helper)
        help.update(points.helper)
        help.update(intersection.helper)

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

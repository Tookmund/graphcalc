help = {'/help' : '[name]: Show usage of command. Without arguments, show all'}

def setup():
        global help
        
        import graph
        help.update(graph.helper)

        import stats 
        help.update(stats.helper)

        import comboandperm 
        help.update(comboandperm.helper)

        import vars
        help.update(vars.helper)

        import sigma
        help.update(sigma.helper)

        import points
        help.update(points.helper)

        import intersection
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
coms = {'/help': helper}

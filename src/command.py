coms = {}
def setup():
        global coms

        import graph
        coms.update(graph.coms)

        import stats
        coms.update(stats.coms)

        import comboandperm
        coms.update(comboandperm.coms)

        import help
        coms.update(help.coms)

        import vars
        coms.update(vars.coms)

        import sigma
        coms.update(sigma.coms)

        import points
        coms.update(points.coms)

        import intersection
        coms.update(intersection.coms)

def command(string):
	str = string.split(" ")
	if str[0] in coms:
		rt = coms[str[0]](str)
		if not (rt is None):
			print("%f" % rt)
			vars.vars['a'] = float(rt)
	else:
		print("%s is not a vaild command" % str[0])


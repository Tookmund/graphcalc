import graph
import stats
import comboandperm
import help
import vars
import sigma
import points

coms = {
	'/help': help.helper,
	'/set': vars.set,
	'/get': vars.get,
	'/graph': graph.graph,
	'/stats': stats.stats,
	'/combo': comboandperm.combo,
	'/perm': comboandperm.perm,
	'/sigma': sigma.sigma,
	'/points': points.plot
}

def command(string):
	str = string.split(" ")
	if str[0] in coms:
		rt = coms[str[0]](str)
		if not (rt is None):
			print("%f" % rt)
			vars.vars['a'] = float(rt)
	else:
		print("%s is not a vaild command" % str[0])


import graph
import eval as evalu 
import stats
import comandper
import help
import vars

parser = evalu.Parser()

def parse(string):
	if string[:1] == '/':
		command(string)

	else:
		try:
			ps = parser.evaluate(string,vars.vars)
			vars.vars['a'] = float(ps)
			print("%f" % ps)
		except:
			print("Failed to parse: %s" % (string))	

coms = {
	'/help': help.helper,
	'/set': vars.set,
	'/get': vars.get,
	'/graph': graph.graph,
	'/stats': stats.stats,
	'/combo': comandper.combo,
	'/perm': comandper.perm
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


import eval
import command
import vars

parser = eval.Parser()

def parse(string):
	if string[:1] == '/':
		command.command(string)

	else:
		try:
			ps = parser.evaluate(string,vars.vars)
			vars.vars['a'] = float(ps)
			print("%f" % ps)
		except:
			print("Failed to parse: %s" % (string))	

	

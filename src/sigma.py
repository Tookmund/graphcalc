import help
import eval
parser = eval.Parser()
helper = {'/sigma' : '<equation> <variable> <start> <end>: Calcuate summation'}

def sigma(args):
	# equation variable start end
	if len(args) < 4:
		help.helper("sigma")
		return None
	eq = args[1]
	var = args[2]
	start = int(float(args[3]))
	end = int(float(args[4]))
	result = 0
	
	# end+1 for inclusive range
	for x in range(start,end+1):
		result += parser.evaluate(eq,{var:x})
	print("%d" % result)

coms = {'/sigma': sigma}

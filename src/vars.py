import help
vars = {}
helper = {'/set' : '<name> <value>: Set variable',
          '/get' : '<name>: Get variable'}

def set(str):
	global vars
	if len(str) < 3:
		help.helper("set")
		return None
	if str[1] == 'x' or str[1] == 'y' or str[1] == 'a':
		print("Unable to set system variables")
	else:
		vars[str[1]] = float(str[2]) 

def get(str):
	if len(str) < 2:
		help.helper("get")
		return None
	global vars
	try:
		return vars[str[1]]
	except:
		pass

coms = {'/set': set,
	'/get': get}

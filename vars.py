import help
vars = {}
def set(str):
	global vars
	if len(str) < 3:
		print("Wrong arguements: "+str(help.help(["","set"])))
	if str[1] == 'x' or str[1] == 'ans':
		print("Unable to set system variables")
	else:
		vars[str[1]] = float(str[2]) 

def get(str):
	if len(str) < 2:
		print("Wrong arguments: /get (name)")
	global vars
	try:
		return vars[str[1]]
	except:
		pass

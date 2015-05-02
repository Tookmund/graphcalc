help = {
'/help' : 'Show this menu',
'/set' : '(name) (value) Set variable',
'/get' : '(name) Get variable',
'/graph' : '(y/x) (equation) (min) (max) Graph a function', 
'/stats' : '(list) Calculate statistics',
'/perm' : '(total) (pick) Calculate permuations',
'/combo' : '(total) (pick) Calulate combinations'
}
def helper(str):
	try:
		com = '/'+str[1]
		print("%s : %s" % (com,help[com]))
	except:
		print("""
Type any expression and it will simplify it to a single number
Ctrl+C to exit
""")
		for x,y in help.items():
			print("%s : %s" % (x,y))

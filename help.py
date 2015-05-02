help = {
'/help' : 'Show this menu',
'/set (name) (value)' : 'Set variable',
'/get (name)' : 'Get variable',
'/graph (y/x) (equation) (min) (max)' : 'Graph a function', 
'/stats (list)' : 'Calculate statistics',
'/perm (total) (pick)' : 'Calculate permuations',
'/combo (total) (pick)' : 'Calulate combinations'
}
def helper(str):
	if str[1]:
		com = '/'+str[1]
		return(help[com])
	else:
		print("""
Type any expression and it will simplify it to a single number
Ctrl+C to exit
"")
		return help

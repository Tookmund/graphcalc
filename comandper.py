from math import factorial as fact

def perm(str):
	total = int(str[1])
	pick = int(str[2])
	return fact(total)/fact(total-pick)

def combo(str):
	total = int(str[1])
	pick = int(str[2])
	return fact(total)/(fact(pick)*fact(total-pick)) 

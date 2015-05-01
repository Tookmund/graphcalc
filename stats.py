import statistics

from statistics import *


def stats(lst):
	list = []
	for x in lst[1:]:
		list.append(int(x))
	#print(list)
	st= {}
	try:
		st["mean"] = mean(list)
		st["standard deviation"] = stdev(list)
		st["median"] = median(list)
		st["mode"] = mode(list)
	except:
		pass
	return st

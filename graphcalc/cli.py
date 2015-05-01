import graphcalc.parser as parser
import graphcalc.graph as graph
import sys

def run():
	graph.setup()
	while True:
		try:
			parser.parse(input("> "))
		except KeyboardInterrupt:
			sys.exit()

import pyser as parser 
import graph
import sys

def run():
        graph.setup()
        print("""Welcome to GraphCalc
To understand how it works type
/help
""")
        while True:
                try:
                        parser.parse(input("> "))
                except KeyboardInterrupt:
                        sys.exit()

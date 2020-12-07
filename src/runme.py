from GraphColouring import GraphColouring
import sys

graph = 'graphs/' + sys.argv[1]
n = int(sys.argv[2])
chi = int(sys.argv[3])

g = GraphColouring(path = graph,
                    pc = 0.8,
                    pm = 0.9,
                    n = n,
                    chi = chi)

g.run()
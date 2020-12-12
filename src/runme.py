from GraphColouringPSO import GraphColouringPSO
import sys

graph = 'graphs/' + sys.argv[1]
n = int(sys.argv[2])
chi = int(sys.argv[3])

g = GraphColouring(path = graph,
                    prob = 0.7,
                    n = n,
                    chi = chi)

g.run()
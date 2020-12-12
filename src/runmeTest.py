from GraphColouringPSO import GraphColouringPSO
from GraphColouringPSOH import GraphColouringPSOH

import sys


graphs = [['myciel3', 11, 4],['myciel4',23,5], ['hexagonal_grid', 20, 3], ['planar_graph', 6, 3], ['planar_graph', 10, 4], ['dodecahedron_schlegel',20,3], ['5-connected_planar', 12, 4], ['5-connected_planar', 28, 4]]

for graph in graphs:
    print('\n' + graph[0] + ' ' + str(graph[2]) + '\n')
    for i in range(100):
        g = GraphColouringPSO(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2])
        g.run()
    print('\n' + graph[0] + ' ' + str(graph[2]+1) + '\n')
    
    for i in range(100):
        g = GraphColouringPSO(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2]+1)
        g.run()
        
    print('\n' + graph[0] + ' ' + str(graph[2]+2) + '\n')

    for i in range(100):
        g = GraphColouringPSO(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2]+2)
        g.run()


print('\n\n\nHIBRIDO\n\n\n')


for graph in graphs:
    print('\n' + graph[0] + ' ' + str(graph[2]) + '\n')
    for i in range(100):
        g = GraphColouringPSOH(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2])
        g.run()
    print('\n' + graph[0] + ' ' + str(graph[2]+1) + '\n')
    
    for i in range(100):
        g = GraphColouringPSOH(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2]+1)
        g.run()
        
    print('\n' + graph[0] + ' ' + str(graph[2]+2) + '\n')

    for i in range(100):
        g = GraphColouringPSOH(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2]+2)
        g.run()
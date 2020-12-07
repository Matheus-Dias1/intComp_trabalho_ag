from GraphColouring import GraphColouring
import sys


graphs = [['myciel4',23,5],['myciel3', 11, 4], ['hexagonal_grid', 20, 3], ['planar_graph', 6, 3], ['planar_graph', 10, 4], ['dodecahedron_schlegel',20,3], ['5-connected_planar', 12, 4], ['5-connected_planar', 28, 4]]

for graph in graphs:
    print('\n' + graph[0] + str(graph[2]) + '\n')
    for i in range(100):
        g = GraphColouring(path = 'graphs/' + graph[0],
                    pc = 0.8,
                    pm = 0.9,
                    n = graph[1],
                    chi = graph[2])
        g.run()
    print('\n' + graph[0] + str(graph[2]+1) + '\n')
    
    for i in range(100):
        g = GraphColouring(path = 'graphs/' + graph[0],
                    pc = 0.8,
                    pm = 0.9,
                    n = graph[1],
                    chi = graph[2]+1)
        g.run()
        
    print('\n' + graph[0] + str(graph[2]+1) + '\n')

    for i in range(100):
        g = GraphColouring(path = 'graphs/' + graph[0],
                    pc = 0.8,
                    pm = 0.9,
                    n = graph[1],
                    chi = graph[2]+2)
        g.run()
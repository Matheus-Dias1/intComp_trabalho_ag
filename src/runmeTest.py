from GraphColouringPSO import GraphColouringPSO
from GraphColouringPSOH import GraphColouringPSOH

import sys


graphs = [['myciel3',11,4]]

# for graph in graphs:
#     print('\n' + graph[0] + ' ' + str(graph[2]) + '\n')
#     f = open('status', 'a')
#     f.write('\n' + graph[0] + ' ' + str(graph[2]) + '\n')
#     for i in range(100):
#         f.close()
#         f = open('status', 'a')
#         f.write(str(i) + ' ')

#         g = GraphColouringPSO(path = 'graphs/' + graph[0],
#                     prob = 0.7,
#                     n = graph[1],
#                     chi = graph[2])
#         g.run()
#     print('\n' + graph[0] + ' ' + str(graph[2]+1) + '\n')
#     f.write('\n' + graph[0] + ' ' + str(graph[2]+1) + '\n')
    
#     for i in range(100):
#         f.close()
#         f = open('status', 'a')
#         f.write(str(i) + ' ')
#         g = GraphColouringPSO(path = 'graphs/' + graph[0],
#                     prob = 0.7,
#                     n = graph[1],
#                     chi = graph[2]+1)
#         g.run()
        
#     print('\n' + graph[0] + ' ' + str(graph[2]+2) + '\n')
#     f.write('\n' + graph[0] + ' ' + str(graph[2]+2) + '\n')

#     for i in range(100):
#         f.close()
#         f = open('status', 'a')
#         f.write(str(i) + ' ')
#         g = GraphColouringPSO(path = 'graphs/' + graph[0],
#                     prob = 0.7,
#                     n = graph[1],
#                     chi = graph[2]+2)
#         g.run()

# print('\n\n\nHIBRIDO\n\n\n')

for graph in graphs:
    print('\n' + graph[0] + ' ' + str(graph[2]) + '\n')
    f = open('status', 'a')
    f.write('\n' + graph[0] + ' ' + str(graph[2]) + '\n')
    for i in range(100):
        f.close()
        f = open('status', 'a')
        f.write(str(i) + ' ')

        g = GraphColouringPSOH(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2])
        g.run()
    print('\n' + graph[0] + ' ' + str(graph[2]+1) + '\n')
    f.write('\n' + graph[0] + ' ' + str(graph[2]+1) + '\n')
    
    for i in range(100):
        f.close()
        f = open('status', 'a')
        f.write(str(i) + ' ')
        g = GraphColouringPSOH(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2]+1)
        g.run()
        
    print('\n' + graph[0] + ' ' + str(graph[2]+2) + '\n')
    f.write('\n' + graph[0] + ' ' + str(graph[2]+2) + '\n')

    for i in range(100):
        f.close()
        f = open('status', 'a')
        f.write(str(i) + ' ')
        g = GraphColouringPSOH(path = 'graphs/' + graph[0],
                    prob = 0.7,
                    n = graph[1],
                    chi = graph[2]+2)
        g.run()
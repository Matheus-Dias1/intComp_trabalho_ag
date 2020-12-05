from Graph import Graph
from random import randint, uniform

class GraphColouring:
    def __init__(self, path, pc, pm, n):
        self.N = n
        self.pm = pm
        self.pc = pc 
        self.graph = Graph(path)
        self.population = [self.randomColors() for i in range(self.N)]
        self.generation = 0
        self.probs = []
        self.expected = []
    
    def randomColors(self):
        res = []
        for i in range(self.graph.numVertices):
            res.append(randint(1,self.graph.chi))
        return res

    def selectByFitness(self):
        # Em caso de empate, pega o primeiro
        fitness = []
        for seq in self.population:
            fitness.append(self.graph.fitnessEvaluation(seq))
        
        return fitness

    def selectSeq(self):
        copy = self.expected.copy()
        b1 = copy.index(min(copy))
        w = copy.index(max(copy))
        copy[b1] = 500000000
        b2 = copy.index(min(copy))
        
        return (b1, b2, w)

    def SPCGX(self, b1, b2):
        res1, res2 = self.graph.conflictingEdges(self.population[b1], self.population[b2])
        print('Seq1 = {}\nSeq2 = {}'.format(res1, res2))
        



    def run(self):
        print('População: ', self.population)
        # Fitness evaluation and selection of two better genes and worst gene sequences
        fitness = self.selectByFitness()
        self.probs = [i/sum(fitness) for i in fitness]
        self.expected = [i*self.N for i in fitness]
        b1, b2, w = self.selectSeq()
        print('melhores: {} e {}'.format(b1,b2))

        pcr = uniform(0,1)
        if pcr > self.pc:
            # Applying SPCGX to b1 and b2
            self.SPCGX(b1, b2)










g =GraphColouring(path = 'in_graph',
                  pc = 0.6,
                  pm = 0.2,
                  n = 5)
g.run()


from Graph import Graph
from random import randint, uniform

class GraphColouring:
    def __init__(self, path, pc, pm, n, chi):
        self.N = n
        self.pm = pm
        self.pc = pc 
        self.graph = Graph(path, chi)
        self.population = [self.randomColors() for i in range(self.N)]
        self.offspring = []
        self.generation = -1
        self.probs = []
        self.expected = []
        self.colouring = []
    
    def randomColors(self):
        res = []
        for i in range(self.graph.numVertices):
            res.append(randint(0,self.graph.chi-1))
        return res

    def getPopulationFitness(self):

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

    def SPCGX(self):
        res1, res2 = self.graph.conflictingEdges(self.offspring[0], self.offspring[1])

        for edge in res1:
            self.offspring[0][edge[1]] = (self.offspring[0][edge[1]] + 1) % self.graph.chi

        for edge in res2:
            self.offspring[1][edge[1]] = (self.offspring[1][edge[1]] + 1) % self.graph.chi

    
    def mutation(self):
        res1, res2 = self.graph.conflictingEdges(self.offspring[0], self.offspring[1])

        for edge in res1:
            if self.offspring[0][edge[0]] == 0:
                self.offspring[0][edge[0]] = self.graph.chi - 1
            else:
                self.offspring[0][edge[0]] -= 1

        for edge in res2:
            if self.offspring[1][edge[0]] == 0:
                self.offspring[1][edge[0]] = self.graph.chi - 1
            else:
                self.offspring[1][edge[0]] -= 1


    def updateWorst(self, w):
        f1 = self.graph.getNumColors(self.offspring[0])
        f2 = self.graph.getNumColors(self.offspring[1])
        fworst = self.graph.getNumColors(self.population[w])

        if f1 < fworst:
            self.population[w] = self.offspring[0]

        if f2 < f1:
            self.population[w] = self.offspring[1]
        

    def isOptimalReached(self):
        res1, res2 = self.graph.conflictingEdges(self.offspring[0], self.offspring[1])

        if res1 == []:
            self.colouring = self.offspring[0]
            return True
        if res2 == []:
            self.colouring = self.offspring[1]
            return True

        return False
        

    def run(self):
        flag = True
        try:
            while True:
                if self.generation >= 1000:
                    flag = False
                    break
                self.generation += 1
                # Fitness evaluation and selection of two better genes and worst gene sequences
                fitness = self.getPopulationFitness()
                self.probs = [i/sum(fitness) for i in fitness]
                self.expected = [i*self.N for i in fitness]
                b1, b2, w = self.selectSeq()
                self.offspring = [self.population[b1], self.population[b2]]

                pcr = uniform(0,1)
                if pcr > self.pc:
                    self.SPCGX()

                pmr = uniform(0,1)
                if pmr > self.pm:
                    self.mutation()
                
                self.updateWorst(w)
                if self.isOptimalReached():
                    break
        except:
            flag = False
        if flag:
            print('\nColoração: {}\nGeração: {}\n'.format(self.colouring, self.generation))
        else: 
            print('Unsuccessful run')





from Graph import Graph
from random import randint, uniform

class GraphColouringPSO:
    def __init__(self, path, prob, n, chi):
        self.N = n
        self.prob = prob
        self.graph = Graph(path, chi)
        # self.particles = [[1, 2, 1, 2, 0, 2], [1, 2, 1, 2, 0, 2], [1, 2, 1, 2, 0, 2]]
        self.particles = [self.randomColors() for i in range(self.N)]
        self.numMovements = -1
        self.colouring = []
    
    def randomColors(self):
        res = []
        for i in range(self.graph.numVertices):
            res.append(randint(0,self.graph.chi-1))
        return res

    def getParticlesFitness(self):

        fitness = []
        for seq in self.particles:
            fitness.append(self.graph.fitnessEvaluation(seq))
        
        return fitness


    def isOptimalReached(self, best):
        conf = self.graph.fitnessEvaluation(self.particles[best])

        if conf == 0:
            self.colouring = self.particles[best]
            return True

        return False

    def getVelocity(self, particle, bestParticle):
        velocity = []
        confEdges, _ = self.graph.conflictingEdges(self.particles[particle])
        confDimensions = [i for (i,_) in confEdges]
        for i, dimension in enumerate(self.particles[particle]):
            if self.particles[particle][i] != self.particles[bestParticle][i] and i in confDimensions:
                probr = uniform(0,1)
                if probr < self.prob:
                    probr = uniform(0,1)
                    if probr > 0.5:
                        velocity.append((i,'+'))
                    else:
                        velocity.append((i,'-'))

            
        return velocity

    def mutation(self, particleindex):
        probr = uniform(0,1)
        if probr > 0.1:
            return
        for _ in range(2):
            dimension = randint(0, len(self.graph.vertices)-1)
            self.changeDimension(self.particles[particleindex], dimension, True)


    def updatePosition(self, particle, velocity):
        candidatePosition = particle
        for i, op in velocity:
            self.changeDimension(candidatePosition, i, op == '+')

        return candidatePosition
                


    def changeDimension(self, particle, dimension, adding):
        if adding:
            particle[dimension] = (particle[dimension] + 1) % self.graph.chi
        else:
            if particle[dimension] == 0:
                particle[dimension] = self.graph.chi - 1
            else:
                particle[dimension] -= 1

        

    def run(self):
        flag = True
        # try:
        while True:
            if self.numMovements >= 5000:
                flag = False

                break
            self.numMovements += 1
            # Fitness evaluation and selection of best particle
            fitness = self.getParticlesFitness()
            best = fitness.index(min(fitness))
            
            for i, particle in enumerate(self.particles):
                if i == best:
                    continue
                velocity = self.getVelocity(i, best)
                candidatePosition = self.updatePosition(particle, velocity)
                if self.graph.fitnessEvaluation(particle) > self.graph.fitnessEvaluation(candidatePosition):
                    self.particles[i] = candidatePosition
                #self.mutation(i)
                if self.graph.fitnessEvaluation(self.particles[best]) > self.graph.fitnessEvaluation(candidatePosition):
                    best = i
                        
            






            if self.isOptimalReached(best):
                flag = True
                break
        # except e:
        #     print(e)
        #     flag = False
        if flag:
            print(self.numMovements)
            #print('\nColoração: {}\nGeração: {}\n'.format(self.colouring, self.numMovements))
        else: 
            print('Unsuccessful run')





class Graph:
    def __init__(self, path, chi):
        self.vertices = []
        self.edges = []
        self.chi = chi
        f = open(path, 'r')
        for index, line in enumerate(f):
            if index == 0:
                self.vertices = line.strip().split(' ')
                self.vertices = [int(i) for i in self.vertices]
            else:
                edge = line.strip().split(' ')
                self.edges.append((int(edge[0]), int(edge[1])))

        f.close()

        self.numVertices = len(self.vertices)


    def conflictingEdges(self, seq1, seq2 = None):
        confEdgesSeq1 = []
        for i, c1 in enumerate(seq1):
            for j, c2 in enumerate(seq1):
                if c1 == c2:
                    if (i, j) in self.edges or (j, i) in self.edges:
                        if (j, i) not in confEdgesSeq1:
                            confEdgesSeq1.append((i,j))

        confEdgesSeq2 = []
        if seq2 != None:
            for i, c1 in enumerate(seq2):
                for j, c2 in enumerate(seq2):
                    if c1 == c2:
                        if (i, j) in self.edges or (j, i) in self.edges:
                            if (j, i) not in confEdgesSeq2:
                                confEdgesSeq2.append((i,j))

        return (confEdgesSeq1, confEdgesSeq2)


    def getNumColors(self, seq):
        unique = []
        for color in seq:
            if color not in unique:
                unique.append(color)

        return len(unique)

    def fitnessEvaluation(self, seq):
        conf = 0
        for i, c1 in enumerate(seq):
            for j, c2 in enumerate(seq):
                if c1 == c2:
                    if (i, j) in self.edges or (j, i) in self.edges:
                        conf += 1
        return int(conf/2)

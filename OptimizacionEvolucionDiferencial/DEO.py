import copy
import numpy as np

class DEO:

    def __init__(self,
                individuals_count,
                dimensions,
                stepsize,
                crossover_rate,
                problem,
                generation_count):
        self.individuals_count = individuals_count
        self.dimensions = dimensions
        self.stepsize = stepsize,
        self.crossover_rate = crossover_rate
        self.problem = problem
        self.generation_count = generation_count
        self.range = self.problem.MAX_VALUE - self.problem.MIN_VALUE

    def run(self):
        self.individuals = np.array([ np.random.random(size = self.dimensions) * self.range - self.problem.MIN_VALUE
            for _ in range(self.individuals_count) ])
        
        generations = []
        generation = 0

        v = []
        u = []
        
        print(f"1: {self.individuals_count}\t 2:{len(self.individuals)}")
        while generation <= self.generation_count:
            for i in range(self.individuals_count):
                r1 = self.randint_excluding([i])
                r2 = self.randint_excluding([i, r1])
                r3 = self.randint_excluding([i, r1, r2])

                v.append( 
                    self.individuals[r1] + self.stepsize * (self.individuals[r2] - self.individuals[r3])
                )
                
                tr = self.randint_excluding([])

                u_vector = []
                for j in range(self.dimensions):
                    rcj = np.random.random()

                    if rcj < self.crossover_rate or j == tr:
                        u_vector.append(v[i][j])
                    else:
                        u_vector.append(self.individuals[i][j])
                u.append(u_vector)

            best = self.individuals[i]
            for i in range(self.individuals_count):
                if self.problem.fitness(u[i]) < self.problem.fitness(self.individuals[i]):
                    self.individuals[i] = copy.deepcopy(u[i])
                
                if self.problem.fitness(self.individuals[i]) < self.problem.fitness(best):
                    best = copy.deepcopy(u[i])

            if generation % 100 == 0:
                print('Generation ', generation, ':', best)
                generations.append(abs(self.problem.fitness(best)))
            generation += 1
        
        return generations

    def randint_excluding(self, used):
        rand = np.random.randint(0, self.individuals_count)
        while rand in used:
            rand = np.random.randint(0, self.individuals_count)
        return rand
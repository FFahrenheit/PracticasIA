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
        self.range = self.problem.MAX_VALUE - self.problem.MIN_VAUE

    def run(self):
        self.individuals = [ np.random.random(size = self.dimensions) * self.range - self.problem.MIN_VAUE
            for _ in range(self.individuals_count) ]
        
        generations = []
        generation = []
        
        while generation <= self.generation_count:
            for i, individual in enumerate(self.individuals):
                pass

            if generation % 100 == 0:
                print('Imprimir y guardar')
            generation += 1
        
        return generations

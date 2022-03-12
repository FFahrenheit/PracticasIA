import numpy as np

class Sphere:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for alelo in cromosoma:
            z += alelo**2
        return z

class Rosenbrock:
    MIN_VALUE = -2.048
    MAX_VALUE = 2.048
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        x = cromosoma       #Alias
        for i in range(len(cromosoma) - 1):
            z += 100 * (x[i+1] - x[i]**2) ** 2 + (x[i] - 1)**2
        return z

class Rastrigin:
    MIN_VALUE = -5.12
    MAX_VALUE = 5.12
    def __init__(self):
        pass
    def fitness(self, cromosoma, A = 10):
        z = A * len(cromosoma)
        for alelo in cromosoma:
            z += alelo**2 - A * np.cos(2 * np.pi * alelo)
        return z

class Quartic:
    MIN_VALUE = -1.28
    MAX_VALUE = 1.28
    def __init__(self):
        pass
    def fitness(self, cromosoma):
        z = 0
        for alelo in cromosoma:
            z += alelo**4
        return z
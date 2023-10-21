import numpy as np
from random import random

class AdalineNeuron:
    def __init__(self, w_quantity:int, expected_output:int):
        self.expected_output = expected_output
        self.w_quantity = w_quantity

    def train(self, data, target_error:float, max_iterations:int, n:float):
        error = 1e10
        w = np.array([random() for _ in range(self.w_quantity)])
        iteration = 0
        self.data = data
        n = n
        self.plot_solution = []

        while error > target_error and iteration < max_iterations:
            error = 0
            for pattern in self.data:
                x1, x2, d = pattern

                d = 1 if d == self.expected_output else 0

                x = np.array([1.0, x1, x2])

                v = np.sum(x*w)

                y = self.activation_function(v)
                e = d - y
                error += e**2

                y_prime = self.activation_derivative(v)

                w = w + n*e*y_prime*x
            
            error /= len(self.data)

            self.plot_solution.append({
                "solution": w,
                "error": error
            })
            iteration += 1
        
        print(f"Entrenamiento de neurona {self.expected_output} finalizado con error {error} en {iteration} iteraciones")
        return self.plot_solution

    def activation_function(self, v):
        # return np.tanh(v)
        return 1/(1 + np.e**(-v))
    
    def activation_derivative(self, v):
        # return (1 - self.activation_function(v))*(1 + self.activation_function(v))
        return self.activation_function(v)*(1 - self.activation_function(v))



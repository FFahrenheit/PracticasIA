import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('dataset_RegresionLineal.txt', delimiter=',')

x = data[:,0]
y = data[:,1]

m = len(x)

a0 = 0
a1 = 0
beta = 0.023
iter_max = 600
convergencia = []

plt.figure(1)
plt.scatter(x, y, color='yellow', edgecolors=['black'], linewidths=[1])

h = a0 + a1 * x
plt.plot(x, h, color='red')

for _ in range(iter_max):
    a0 = a0 - beta * ((1/m) * sum(h-y))
    a1 = a1 - beta * ((1/m) * sum(np.multiply(h - y, x)))

    h = a0 + a1 * x;

    J = (1/(2*m)) * sum( np.power(h - y, 2))
    convergencia.append(J)

plt.plot(x, h, color='green')

plt.figure(2)
plt.plot(convergencia)

dato_entrada = 9.7687
h_dato_entrada = a0 + a1 * dato_entrada
plt.figure(1)
plt.scatter(dato_entrada, h_dato_entrada, color='magenta', linewidths=[3])

print(f"J = {J:.6f}\ta0 = {a0:.6f}\t a1 = {a1:.6f}\t")
print(f"x = {dato_entrada:.6f}\t y = 7.543500\t h = {h_dato_entrada:.6f}")
plt.show()

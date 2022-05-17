import numpy as np
import matplotlib.pyplot as plt

# Data load
data = np.loadtxt('dataset_RegresionLinealMultivariable.txt', delimiter=',')

x = data[:,0:2]
y = data[:,2]
x_datos = x

m = len(x)
n = len(x[0])

# Original data plot
fig = plt.figure(0)
ax = fig.add_subplot(projection='3d')
ax.scatter(x[:,0], x[:,1], y,color='yellow', edgecolors=['black'], linewidths=[1])
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')


# Normalization
x_norm = np.zeros((m, n))
mu = np.mean(x, axis=0)
sigma = np.std(x, axis=0)

for i in range(n):
    x_norm[:,i] = (x[:,i] - mu[i])/sigma[i]

fig = plt.figure(1)
ax = fig.add_subplot(projection='3d')
ax.scatter(x[:,0], x[:,1], y,color='yellow', edgecolors=['black'], linewidths=[1])
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

x = x_norm
x = np.hstack((np.ones((m, 1)), x))
n = n + 1

a = np.zeros(n)
beta = 0.8
iter_max = 600
h = []
convergencia = []

for i in range(m):
    h.append(np.dot(np.transpose(a), x[i]))

J = (1/(2*m)) * sum( np.power(h - y, 2))

for _ in range(iter_max):
    convergencia.append(J)

    for j in range(n):
        a[j] = a[j] - beta*(1/m)*np.sum((h-y) * x[:,j]) 

    for i in range(m):
        h[i] = np.dot(np.transpose(a), x[i])

    J = (1/(2*m)) * sum( np.power(h - y, 2))
    convergencia.append(J)

plt.figure(2)
plt.plot(convergencia)

print(f"J = {J}\ta0 = {a[0]}\ta1 = {a[1]}\ta2 = {a[2]}\n");

for prueba, i in enumerate(range(4,7)):
    print(f"Dato de prueba {prueba+1}\tx1 = {x_datos[i,0]}\tx2 = {x_datos[i,1]}\tSalida correcta y = {y[i]}\t Prediccion h = {h[i]}\n");

plt.show()
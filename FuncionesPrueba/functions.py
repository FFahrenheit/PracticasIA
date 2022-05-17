import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm

class TestFunctions:
    def __init__(self):
        pass

    def plot_3d(self, X, Y, Z):
        fig = plt.figure()
        ax = fig.add_subplot(projection = '3d')
        surf = ax.plot_surface(X, Y,  Z, cmap = cm.coolwarm, linewidth=1)
        fig.colorbar(surf)
        plt.show()

    def arange(self, n, rang):
        result = []
        for _ in range(n):
            result.append(np.arange(-1 * rang, rang, 0.1))
        return result
     
    def sphere(self, n, rang):
        X, Y = self.arange(n, rang)
        X, Y = np.meshgrid(X, Y)
        Z = self.get_sphere([X, Y])
        self.plot_3d(X, Y, Z)

    def get_sphere(self, dimentions):
        result = 0
        for x in dimentions:
            result += x**2
        return result

    def rosenbrock(self, n, rang):
        X, Y = self.arange(n, rang)
        X, Y = np.meshgrid(X, Y)
        Z = self.get_rosenbrock([X, Y])
        self.plot_3d(X, Y, Z)

    def get_rosenbrock(self, dimentions):
        x = dimentions
        result = 0
        for i in range(len(dimentions)-1):
            result += 100 * (x[i+1] - x[i]**2) ** 2 + (x[i] - 1)**2
        return result

    def rastringin(self, n, rang):
        X, Y = self.arange(n, rang)
        X, Y = np.meshgrid(X, Y)
        Z = self.get_rastringin([X, Y])
        self.plot_3d(X, Y, Z)

    def get_rastringin(self, dimentions, A = 10):
        result = A * len(dimentions)
        print(result)
        for x in dimentions:
            result += x**2 - A * np.cos(2 * np.pi * x)
        return result
    
    def quartic(self, n, rang):
        X, Y = self.arange(n, rang)
        X, Y = np.meshgrid(X, Y)
        Z = self.get_quartic([X, Y])
        self.plot_3d(X, Y, Z)

    def get_quartic(self, dimentions):
        result = 0
        for x in dimentions:
            result += x**4
        return result
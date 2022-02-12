from mpl_toolkits.mplot3d import Axes3D
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
        for d in dimentions:
            result += d**2
        return result
    
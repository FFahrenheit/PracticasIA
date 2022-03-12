import functions
import AGC
import matplotlib.pyplot as plt

funciones = [
    functions.Sphere,
    functions.Rosenbrock,
    functions.Rastrigin,
    functions.Quartic
]
dimensiones = [2, 4, 8]
generaciones = [i for i in range(0, 2001, 100)]
numero_ejecuciones = 5
colors = { 2: 'r', 4: 'g', 8: 'b' }

def main():

    for funcion in funciones:
        promedios = []

        for dimension in dimensiones:
            ejecuciones = []
            for _ in range(numero_ejecuciones):
                s = funcion()
                ag = AGC.AGC(64, dimension , 2000, 0.02, s, False)
                ejecuciones.append(ag.run())

            promedio = get_promedios(ejecuciones)
            promedios.append(promedio)
            
            _, ax = plt.subplots(1)
            ax.plot(generaciones, promedio, colors[dimension])
            plt.title(f"{funcion.__name__} de {dimension} dimensiones")
            # ax.set_ylim(ymin=0)
            plt.show()
        
        _, ax = plt.subplots(1)
        [ plt.plot(generaciones, promedios[index], colors[dimension], 
            label = f"{dimension} Dimensiones") for index, dimension in enumerate(dimensiones)]
        ax.legend(loc='upper right', frameon = False)
        # ax.set_ylim(ymin=0)
        plt.title(f"{funcion.__name__}")
        plt.show()

def get_promedios(ejecuciones):
    promedios = [0 for _ in range(len(ejecuciones[0]))]
    for i in range(len(ejecuciones[0])):
        for ejecucion in ejecuciones:
            promedios[i] += ejecucion[i]
        promedios[i] /= len(ejecuciones)
    return promedios

if __name__ == '__main__':
    main()

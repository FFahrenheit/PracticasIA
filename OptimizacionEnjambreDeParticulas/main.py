import functions
import PSO
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
                rango = s.MAX_VALUE - s.MIN_VALUE
                cantidad_individuos = 30
                ro = 8
                phi1_max = 1.7
                phi2_max = 2.0
                v_max = rango * 0.01
                n_generaciones = 2000

                pso = PSO.PSO(cantidad_individuos, dimension, ro, phi1_max, phi2_max, v_max, s, n_generaciones)
                ejecuciones.append(pso.run())

            promedio = get_promedios(ejecuciones)
            promedios.append(promedio)
            
            _, ax = plt.subplots(1)
            print(generaciones)
            print(promedio)

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

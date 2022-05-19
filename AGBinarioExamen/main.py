import examen
import AG

def main():
    objetos = [13, 8, 25, 4, 18, 6, 33, 22, 45, 11, 76, 10, 1]
    # objetos *= 5

    individuos = 50
    alelos = len(objetos)
    tamano_gen = 1
    generaciones = 100
    factor_mutacion = 0.01
    altura_L = 211
    pila = examen.PilaFiguras(objetos, altura_L)
    
    ag = AG.AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, pila)
    respuesta = ag.run()

    print('-' * 80)
    print("\tSeleccion final")
    
    peso = 0
    for index, objeto in enumerate(objetos):
        if respuesta[index]:
            print(f"Objeto {index}:\t +{objeto}")
            peso += objeto
    
    print('-'*30)
    print(f"Peso total:\t {peso}\n({peso}/{altura_L}, {round(peso/altura_L*100,2)}% del tamaño maximo)")

if __name__ == '__main__':
    main()

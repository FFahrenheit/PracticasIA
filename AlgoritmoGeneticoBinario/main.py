import coins
import AG

def main():
    monedas = [ 1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20, 20, 20, 5, 1, 1, 20,
    20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1, 20, 10, 5, 5, 20, 2, 10, 1, 2, 5, 10, 20, 10, 2,
    5, 5, 20, 1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2, 10, 20, 2, 10, 10, 20, 5, 10, 1, 2, 1, 5,
    20, 2, 5, 1, 5, 10, 2, 5, 10, 2, 1, 1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2 ]

    individuos = 64
    alelos = len(monedas)
    tamano_gen = 2
    generaciones = 2_000
    factor_mutacion = 0.01
    fila = coins.Coins(monedas, sum(monedas))
    
    ag = AG.AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, fila)
    final = ag.run()

    posiciones = {}
    tomadas = {}
    total_tomado = 0
    for i, valor in enumerate(monedas):
        if valor in posiciones:
            posiciones[valor].append(i)
        else:
            posiciones[valor] = [ i ]
        
        if final[i]:
            total_tomado += valor
            if valor in tomadas:
                tomadas[valor].append(i)
            else:
                tomadas[valor] = [ i ]

    for k in sorted(posiciones):
        total = len(posiciones[k])
        tomada = len(tomadas.get(k, []))
        porcentaje = round(tomada/total * 100, 2)
        print(f"${k}\t {tomada}/{total}\t {porcentaje}%\t ${tomada * k}")
    
    total_tomadas = len([None for moneda in final if moneda == 1])
    print(f"Total: ${total_tomado}. {total_tomadas}/{len(monedas)} = {round(total_tomadas/len(monedas)*100,2)}%")

def test():
    monedas = [ 1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20, 20, 20, 5, 1, 1, 20,
    20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1, 20, 10, 5, 5, 20, 2, 10, 1, 2, 5, 10, 20, 10, 2,
    5, 5, 20, 1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2, 10, 20, 2, 10, 10, 20, 5, 10, 1, 2, 1, 5,
    20, 2, 5, 1, 5, 10, 2, 5, 10, 2, 1, 1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2 ]

    fila = coins.Coins(monedas, sum(monedas))
    p1 = [1 for i in range(len(monedas))]

    print(f"{p1} = {fila.f(2, p1)}")

if __name__ == '__main__':
    # test()
    main()

import coins
import AG

def main():
    monedas = [ 1, 20, 5, 1, 2, 5, 5, 1, 5, 2, 2, 1, 10, 5, 10, 5, 20, 20, 20, 5, 1, 1, 20,
    20, 1, 10, 2, 10, 5, 2, 10, 1, 20, 1, 20, 10, 5, 5, 20, 2, 10, 1, 2, 5, 10, 20, 10, 2,
    5, 5, 20, 1, 1, 5, 10, 10, 10, 1, 5, 2, 1, 2, 10, 20, 2, 10, 10, 20, 5, 10, 1, 2, 1, 5,
    20, 2, 5, 1, 5, 10, 2, 5, 10, 2, 1, 1, 1, 10, 20, 10, 20, 2, 2, 10, 20, 10, 1, 1, 5, 2 ]

    individuos = 50
    alelos = len(monedas)
    tamano_gen = 1
    generaciones = 2_500
    factor_mutacion = 0.01
    fila = coins.Coins(monedas)
    
    ag = AG.AG(individuos, alelos, tamano_gen, generaciones, factor_mutacion, fila)
    final = ag.run()

    posiciones = {}
    tomadas = {}
    total_tomado = 0
    suma = sum(monedas)
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
    print('#'*55)
    
    print("Moneda\t\tTomadas\t\tPorcentaje\tTotal")
    for k in sorted(posiciones):
        total = len(posiciones[k])
        tomada = len(tomadas.get(k, []))
        porcentaje = round(tomada/total * 100, 2)
        print(f"${k}\t\t{tomada}/{total}\t\t{porcentaje}%\t\t${tomada * k}")
    
    total_tomadas = len([None for moneda in final if moneda == 1])
    print('-'*55)
    print(f"Monedas\t\t{total_tomadas}/{len(monedas)}\t\t{round(total_tomadas/len(monedas)*100,2)}%\t\t${total_tomado}")
    print(f"Valor\t\t{total_tomado}/{suma}\t\t{round(total_tomado/suma*100, 2)}%\t\t${total_tomado}")
    print(f"Maximo\t\t{len(monedas)}/{len(monedas)}\t\t100.00%\t\t${suma}")

if __name__ == '__main__':
    main()

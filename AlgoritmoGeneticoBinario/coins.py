class Coins:
    def __init__(self, denominaciones, suma):
        self._suma = suma
        self._denominaciones = denominaciones

    def f(self, longitud_gen, cromosoma):

        total = self._suma
        ultimo = False
        ultimo_restado = False
        ultimo_valor = 0 
        juntos = 1
        
        for n, (i, j) in enumerate(zip(cromosoma[::2], cromosoma[1::2])):
            x = n*2         #Indice i  
            y = n*2 + 1     #Indice j

            if i and j:
                total -= (self._denominaciones[x] + self._denominaciones[y])
                ultimo = True
                ultimo_restado = True
                juntos += 1
                ultimo_valor = self._denominaciones[y]

            elif not i and not j:
                total -= (self._denominaciones[x] + self._denominaciones[y]) 
                ultimo = False
            
            elif i:
                if ultimo:
                    if ultimo_restado:
                        total -= self._denominaciones[x]
                    else:
                        total -= (self._denominaciones[x] + ultimo_valor)
                    juntos += 1
                ultimo = False
            
            elif j:
                ultimo = True
                ultimo_valor = self._denominaciones[y]
                ultimo_restado = False

        return total / juntos

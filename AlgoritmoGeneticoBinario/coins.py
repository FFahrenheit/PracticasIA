class Coins:
    def __init__(self, denominaciones):
        self._denominaciones = denominaciones

    def f(self, longitud_gen, cromosoma):
        total = 0
        juntos = 1
        anterior = False
        for index, gen in enumerate(cromosoma):
            if gen:
                total += self._denominaciones[index]
                if anterior:
                    juntos += 1
                anterior = True
            else:
                anterior = False

        return total ** (1/juntos)


class PilaFiguras:
    def __init__(self, tamaños, maxima_altura):
        self.tamaños = tamaños
        self.maxima_altura = maxima_altura

    def f(self, longitud_gen, cromosoma):
        altura = 0
        for index, gen in enumerate(cromosoma):
            if gen:
                altura += self.tamaños[index]
        
        diferencia = altura - self.maxima_altura
        if diferencia > 0:
            return altura /(diferencia+1)
        
        return altura
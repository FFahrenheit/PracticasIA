import functions
import AGC

INDIVIDUOS = 64
ALELOS = 2
GENERACIONES = 2_000
MUTACION = 0.02
ISMAX = False

def main():
    s = function.Sphere()
    ag = AGC.AGC(64, 2 , 2000, 0.02, s, False)
    ag.run()

if __name__ == '__main__':
    main()

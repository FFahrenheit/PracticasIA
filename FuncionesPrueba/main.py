from functions import TestFunctions

def main():
    functions = TestFunctions()

    functions.sphere(2, 5.12)
    functions.rosenbrock(2, 2.048)
    functions.rastringin(2, 5.12)
    functions.quartic(2, 1.28)

if __name__ == '__main__':
    main()
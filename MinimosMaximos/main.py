import numpy as np
import matplotlib.pyplot as plt

def process(polynomial : list):
    poly = np.poly1d(polynomial)                          #Convert to polynomial: y

    first_derivative = np.polyder(poly, 1)
    second_derivative = np.polyder(poly, 2)         #Get y' and y''

    roots = np.roots(first_derivative)              #Solutions to y'
    values = np.polyval(poly, roots)                #Evaluate y to the solutions to y'
    values_2d = np.polyval(second_derivative, roots)#Evaluate y'' to the solutions to y'

    max = np.max(roots) + 0.5                       #Max value to plot +x
    min = np.min(roots) - 0.5                       #Min value to plot -x
    x = np.linspace(min, max, 100)                  #Domain
    y = np.polyval(poly, x)                         #Range

    plt.plot(x, y, 'r')                             #Plot x,y
    plt.plot(roots, values, '*')                    #Plot min and max
    
    plt.title(                                      #Prin title
        ''.join([f"{'+' if v >= 0 else ''}{v}x^{len(polynomial) - i - 1}" 
            for i,v in enumerate(polynomial)]))     
    
    [ plt.annotate(                                 #Print points
        f"{'Minimo' if v[1] > 0 else 'Maximo' if v[1] < 0 else 'Inflexion'}({k:.2f}, {v[0]:.2f})", (k, v[0]))
            for k,v in dict(zip(roots, zip(values, values_2d))).items() ]
    
    plt.show()                                      #Show plot

def main():
    poly = [1, -4, 1, 6]
    process(poly)

if __name__ == '__main__':
    main()
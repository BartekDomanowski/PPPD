import matplotlib.pyplot as plt
import random, math
random.seed(123)


def srednia_listy(lista): 
    n = len(lista)
    suma = 0 
    # for element in lista: 
    #     suma += element
    for i in range(len(lista)): 
        suma += lista[i]
    return (suma / n)


def regresja(x, y): 
    n = len(x)
    srednia_x = srednia_listy(x)
    srednia_y = srednia_listy(y)
    beta = 0 
    for i in range(n):
        beta += ((x[i] - srednia_x)*(y[i] - srednia_y)) / ((x[i] - srednia_x) ** 2)
    alfa = srednia_y - beta * srednia_x
    return [alfa, beta]


# lista 5- cio elementowa
# 0    1   2 3 4
# 3.14 2.1 2 2 2


def main(): 
    random.seed(123)
    alpha0 = -3
    beta0 = 1.5
    n = 100
    x = [ random.uniform(-10, 10) for i in range(n) ]
    y = [ alpha0+beta0*x[i]+random.normalvariate(0, 1) for i in range(n) ]
    wspolczynniki_regresji = regresja(x, y)
    plt.scatter(x, y)
    # rysowanie odcinka [xmin, xmax], [ymin, ymax]:
    plt.plot([-10, 10], [alpha0+beta0*(-10), alpha0+beta0*10], color="red")
    # zapis do pliku PNG:
    plt.savefig("zadanie_5_01.png")


if __name__ == "__main__": 
    main()
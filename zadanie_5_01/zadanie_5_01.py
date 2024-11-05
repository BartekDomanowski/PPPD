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


def E(alpha, beta, x, y): 
    n = len(x)
    wynik = 0
    for i in range(n):
        wynik += ((alpha + beta * x[i] - y[i]) ** 2)
    return wynik


def odchylenie_standardowe_listy(lista): 
    srednia = srednia_listy(lista)
    gora = 0
    n = len(lista)
    for i in range(n): 
        gora += ((lista[i] - srednia) ** 2)
    return math.sqrt(gora / n)


def r(x, y): 
    n = len(x)
    srednia_x = srednia_listy(x)
    srednia_y = srednia_listy(y)
    s_x = odchylenie_standardowe_listy(x)
    s_y = odchylenie_standardowe_listy(y)
    suma = 0
    for i in range(n): 
        suma += (((x[i] - srednia_x) * (y[i] - srednia_y)) / (s_x * s_y))
    return (1/(n-1)) * suma


# lista 5- cio elementowa
# 0    1   2 3 4
# 3.14 2.1 2 2 2


def main(): 
    alpha0 = -3
    beta0 = 1.5
    n = 100
    x = [ random.uniform(-10, 10) for i in range(n) ]
    y = [ alpha0+beta0*x[i]+random.normalvariate(0, 1) for i in range(n) ]
    wspolczynniki_regresji = regresja(x, y)
    alfa = wspolczynniki_regresji[0]
    beta = wspolczynniki_regresji[1]
    # plt.scatter(x, y)
    # # rysowanie odcinka [xmin, xmax], [ymin, ymax]:
    # plt.plot([-10, 10], [alpha0+beta0*(-10), alpha0+beta0*10], color="red")
    # # zapis do pliku PNG:
    # plt.savefig("zadanie_5_01.png")


if __name__ == "__main__": 
    main()
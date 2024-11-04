import matplotlib.pyplot as plt
import random, math
random.seed(123)


def srednia_arytmetyczna_listy(lista: list[int]) -> int: 
    suma: int = 0
    for i in range(len(lista)): 
        suma += lista[i]
    return suma / len(lista)


def regresja(x: list[int], y: list[int]) -> list[int]: 
    n: int = len(x) # obie listy mają równą długość
    beta: float = 0
    x_srednia: float = srednia_arytmetyczna_listy(x)
    y_srednia: float = srednia_arytmetyczna_listy(y)
    for i in range(1, n): 
        beta += ((x[i] - x_srednia) * (y[i] - y_srednia)) / ((x[i] - x_srednia) ** 2)
    alpha: float = y_srednia - beta * x_srednia 
    return [alpha, beta]


def E(alpha: float, beta: float, x: list[int], y: list[int]) -> float: 
    n: int = len(x) # obie listy mają równą długość
    wspolczynnik_E: float = 0
    for i in range(n):
        wspolczynnik_E += ((alpha + beta * x[i] - y[i]) ** 2)
    return wspolczynnik_E


def odchylenie_standardowe_listy(lista: list[int]) -> float:
    suma: float = 0
    n: int = len(lista)
    srednia_listy: float = srednia_arytmetyczna_listy(lista)
    for i in range(n): 
        suma += ((lista[i] - srednia_listy) ** 2)
    odchylenie_standardowe: float = math.sqrt(suma / n)
    return odchylenie_standardowe


def r(x: list[int], y: list[int]) -> float: 
    odchylenie_stadardowe_x = odchylenie_standardowe_listy(x)
    odchylenie_stadardowe_y = odchylenie_standardowe_listy(y)   
    x_srednia: float = srednia_arytmetyczna_listy(x)
    y_srednia: float = srednia_arytmetyczna_listy(y)
    n: int = len(x)
    suma: float = 0
    for i in range(n): 
        suma += ((x[i] - x_srednia) / odchylenie_stadardowe_x) * ((y[i] - y_srednia) / odchylenie_stadardowe_y)
    wspolczynnik_r: float = ((1/(n-1)) * suma)
    return wspolczynnik_r


def main(): 
    alpha0 = -3
    beta0 = 1.5
    n = 100
    x = [ random.uniform(-10, 10) for i in range(n) ]
    y = [ alpha0+beta0*x[i]+random.normalvariate(0, 1) for i in range(n) ]
    # wykres rozproszenia:
    plt.scatter(x, y)
    # rysowanie odcinka [xmin, xmax], [ymin, ymax]:
    plt.plot([-10, 10], [alpha0+beta0*(-10), alpha0+beta0*10], color="red")
    # zapis do pliku PNG:
    plt.savefig("zadanie_5_01.png")


if __name__ == "__main__": 
    main()
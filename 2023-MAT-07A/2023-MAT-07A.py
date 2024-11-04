import random
import math


def generuj_sygnal(n, seed):
    """
    Generuje `n` punktów z procesu błądzenia losowego o kroku pochodzącym z rozkładu normalnego.
    Punktem startowym jest 0. Dla danej wartości `seed` generuje zawsze te same wartości.
    """
    random.seed(seed)
    x = [0.0] * n
    x[0] = 0.0
    for i in range(1, n):
        x[i] = x[i - 1] + random.normalvariate(0, 1)
    return x


def wypisz(sygnal):
    """
    Wypisuje listę liczb `sygnal` w formacie zmiennopozycyjnym, z dwiema cyframi po przecinku.
    """
    print('[', end='')
    for i in range(len(sygnal)):
        print(f'{sygnal[i]:.2f}', end='' if i == len(sygnal) - 1 else ', ')
    print(']')


def kwantyzuj(x: list[float], k: int):
    mini: float = float("inf")
    maks: float = float("-inf")
    for element in x: 
        if element < mini: 
            mini = element
        if element > maks:
            maks = element
    t: list[float] = [0] * (k + 1)
    t[0] = mini
    t[k] = maks
    roznica: float = maks / k
    for i in range(1, k):
        t[i] = t[i - 1] + roznica
    a: list[float] = [0] * len(x)
    for i in range(len(x)):
        if x[i] == maks:
            a[i] = k - 1
        else:
            for j in range(len(t) - 1):
                if t[j] <= x[i] and x[i] < t[j + 1]:
                    a[i] = j
    return a, t      


def stworz(x: list[float], a: list[float]) -> list[float]:
    mini: float = float("inf")
    maks: float = float("-inf")
    for element in a: 
        if element < mini: 
            mini = element
        if element > maks:
            maks = element
    y: list[float] = [ 0 for i in range(len(x)) ]
    for i in range(mini, maks + 1):
        aktualna_suma = 0
        aktualny_licznik_elementow = 0
        for j in range(len(x)): 
            if a[j] == i: 
                aktualna_suma += x[j]
                aktualny_licznik_elementow += 1
        if aktualny_licznik_elementow > 0: 
            aktualna_srednia = aktualna_suma / aktualny_licznik_elementow
            for j in range(len(a)): 
                if a[j] == i: 
                    y[j] = aktualna_srednia
    return y
        

def blad(x: list[float], y: list[float]) -> float:
    suma: float = 0.0
    n: int = len(x)
    for i in range(n):
        suma += ((x[i] - y[i]) ** 2)
    return math.sqrt((1/n) * suma)
        

def main() -> None:
    n: int = int(input("Podaj n: "))
    k: int = int(input("Podaj k: "))
    seed: int = int(input("Podaj ziarno: "))
    if n < 1 or k < 0:
        raise ValueError("Błędne dane")
    x: list[float] = generuj_sygnal(n, seed)
    print("x: ", end = "")
    wypisz(x)
    t: list[float]
    a: list[float]
    a, t = kwantyzuj(x, k)
    print("t: ", end = "")
    wypisz(t)
    print("a: ", end = "")
    wypisz(a)
    y: list[float]
    y = stworz(x, a)
    print("y: ", end = "")
    wypisz(y)
    for nowe_k in range(2, (n // 2) + 1, 2): #patrząc na przykład raczej chodziło o n // 2 niz n // 4
        print(f"***dla k={nowe_k}:")
        print("x: ", end = "")
        wypisz(x)
        a, t = kwantyzuj(x, nowe_k)
        y = stworz(x, a)
        print("y: ", end = "")
        wypisz(y)
        print(f"Średni błąd wynosi {blad(x,y):.3f}")


if __name__ == "__main__":
    main()
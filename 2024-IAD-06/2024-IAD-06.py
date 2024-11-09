import random
import matplotlib.pyplot as plt
import math
random.seed(711)


def rysuj(x_train, y_train, label_train, x_test, y_test):
    # Rysowanie wykresów punktów treningowych i przykładowych punktów testowych
    x_red = [x_train[i] for i in range(len(label_train)) if label_train[i] == 1]
    x_green = [x_train[i] for i in range(len(label_train)) if label_train[i] == 0]
    y_red = [y_train[i] for i in range(len(label_train)) if label_train[i] == 1]
    y_green = [y_train[i] for i in range(len(label_train)) if label_train[i] == 0]
    plt.scatter(x_red, y_red, c = "red", s = 60, alpha=0.5, label = "1")
    plt.scatter(x_green, y_green, c = "green", s = 60, alpha=0.5, label = "0")
    plt.scatter(x_test, y_test, c = "black", s = 70, label = 'test')
    plt.title("Zbiór punktów treningowych z przykładowymi punktami testowymi")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(title = "Etykieta")
    plt.savefig("zbior_treningowy_testowy.png")
    plt.show()


def losuj_lista(n: int, a: int = -1, b: int = 1) -> list[float]:
    lista: list[float] = [[0,0]] * n
    for i in range(n): 
        liczba_1 = random.uniform(a, b)
        liczba_1 = round(liczba_1, 2)
        lista[i] = liczba_1
    return lista


def przypisz_etykiete(x_col: list[float], y_col: list[float], threshlod: float = 1) -> list[int]: 
    etykiety: list[int] = [0] * len(x_col)
    for i in range(len(x_col)): 
        if abs(x_col[i] - y_col[i]) <= threshlod: 
            etykiety[i] = 1
        else:
            etykiety[i] = 0 
    return etykiety


def dystans(x1: float, y1: float, x2: float, y2: float) -> float: 
    return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )


def kNN(x1: float, y1: float, x_col: list[float], y_col: list[float], labels: list[int], k: int = 3) -> int:
    sasiedzi: list[(float, float, float, int)] = [ (dystans(x1, y1, x_col[i], y_col[i]), x_col[i], y_col[i], labels[i]) for i in range(len(x_col)) ]
    licznik_do_k: int = 1
    ile_0: int = 0
    ile_1: int = 0
    etykieta: int = -1
    for sasiad in sorted(sasiedzi):
        if sasiad[3] == 1: 
            ile_1 += 1
        else: 
            ile_0 += 1
        licznik_do_k += 1
        if licznik_do_k == k: 
            break
    if ile_0 > ile_1: 
        etykieta = 0
    elif ile_1 > ile_0: 
        etykieta = 1
    else: 
        etykieta = random.randint(0,1)
    return etykieta


def zapisz_dane(x_col: list[float], y_col: list[float], labels: list[int]) -> None:
    with open("wynik.txt", "w") as out_file: 
        print("x y label", file = out_file)
        for i in range(len(x_col)): 
            print(x_col[i], y_col[i], labels[i], file = out_file)
    print("Zapisywanie danych treningowych\nDane zapisano pomyślnie!")


def main() -> None: 
    print("Generowanie danych treningowych")
    punkty_treningowe: int = int(input("Podaj liczbę punktów treningowych do wygenerowania: "))
    while punkty_treningowe <= 0: 
        punkty_treningowe = int(input("Podaj liczbę punktów treningowych do wygenerowania: "))
    lewy_zakres_losowania: float = float(input("Podaj lewy zakres przedziału, z których mają być losowane punkty: "))
    prawy_zakres_losowania: float = float(input("Podaj prawy zakres przedziału, z których mają być losowane punkty: "))
    if int(lewy_zakres_losowania) != lewy_zakres_losowania or int(prawy_zakres_losowania) != prawy_zakres_losowania:
        raise ValueError("Błędny przedział!")
    x_col: list[float] = losuj_lista(punkty_treningowe, lewy_zakres_losowania, prawy_zakres_losowania)
    y_col: list[float] = losuj_lista(punkty_treningowe, lewy_zakres_losowania, prawy_zakres_losowania)
    treshold: int = int(input("Podaj wartość threshold: "))
    labels: list[int]  = przypisz_etykiete(x_col, y_col, treshold)
    print("Testowanie algorytmu kNN")
    flag: bool = True
    #ten fragment jest tylko i wyłącznie dla potrzeby wygenerowania wykresu i nie jest częścią rozwiązania
    x_test: list[float] = []
    y_test: list[float] = []
    #ten fragment jest tylko i wyłącznie dla potrzeby wygenerowania wykresu i nie jest częścią rozwiązania
    wsp_x: float
    wsp_y: float
    liczba_sasiadow: int
    aktualna_etykieta: int
    kontynuuj: bool
    while flag: 
        wsp_x = float(input("Podaj współrzędną x-ową: "))
        wsp_y = float(input("Podaj współrzędną y-ową: "))
        #ten fragment jest tylko i wyłącznie dla potrzeby wygenerowania wykresu i nie jest częścią rozwiązania
        x_test.append(wsp_x)
        y_test.append(wsp_y)
        #ten fragment jest tylko i wyłącznie dla potrzeby wygenerowania wykresu i nie jest częścią rozwiązania
        liczba_sasiadow = int(input("Podaj liczbę sąsiadów, którą chcesz rozpatrywać: "))
        while liczba_sasiadow <= 0: 
            liczba_sasiadow = int(input("Podaj dodatnia liczbę sąsiadów, którą chcesz rozpatrywać: "))
        aktualna_etykieta = kNN(wsp_x, wsp_y, x_col, y_col, labels, liczba_sasiadow)
        print(f"Punkt ({wsp_x:.1f}, {wsp_y:.1f}) otrzymał etykietę {aktualna_etykieta}.")
        kontynuuj = input("Czy chcesz kontynuować testowanie? [y/n]\n") 
        if kontynuuj== "n": 
            flag = False
        elif kontynuuj == "y":
            continue
        else: 
            raise Exception("Błąd! Nieznana wartość.")
    zapisz_dane(x_col, y_col, labels)
    rysuj(x_col, y_col, labels, x_test, y_test)
        

if __name__ == "__main__": 
    main()
import math, random

def drzewo(x: int, y: int) -> bool:
    if x >= 0 and x <= 10 and y >= 0 and y <= 10:
        return (x == y) and (x % 10 < 4 or x % 10 > 5)
    elif x >= -10 and x <= -1 and y >= 0 and y <= 10:
        return True
    else:
        return False
    

def drzewo2(x: int, y: int ) -> bool:
    if x >= 0 and x <= 10 and y >= -10 and y <= 10:
        liczba: float = random.random()
        if liczba <= 0.5: 
            return True
        else: 
            return False
    elif x >= -10 and x <= -1 and y >= -10 and y <= 10:
        liczba: float = random.random()
        if liczba <= 0.1: 
            return True
        else: 
            return False
    else: 
        return False
    

def wypisz_kolo(x: int, y: int, r: int) -> None: 
    print(f"Srodek ({x},{y}), promien {r}")


def najmniejszy_plot(x_sad: int, y_sad: int, r_sad: int, x: int, y: int) -> float:
    najwieksza_odleglosc: float = -float("inf")
    for i in range(y_sad + r_sad, y_sad - r_sad - 1, -1):
        for j in range(x_sad - r_sad, x_sad + r_sad + 1): 
            if ((i - y_sad)**2 + (j - x_sad)**2) <= r_sad**2 and drzewo(i,j):
                najwieksza_odleglosc = max(najwieksza_odleglosc, math.sqrt((x-j)**2 + (y-i)**2))
    return round(najwieksza_odleglosc, 5)


def zapisz_do_pliku(sciezka: str, x: int, y: int, r: int) -> None:
    with open(sciezka, "w") as out_file:
        for i in range(y + r, y - r - 1, -1):
            print(f"{i:<4}", end = "", file = out_file)
            for j in range(x - r, x + r + 1): 
                if ((i - y)**2 + (j - x)**2) <= r**2:
                    if drzewo(i,j):
                        print("D", end = "", file = out_file)
                    else:
                        print("*", end = "", file = out_file)
                else:
                    print(" ", end = "", file = out_file)
            print(file = out_file)
            if i == y - r:
                print("y/x ", end = "", file = out_file)
                for m in range(x - r, x + r + 1):
                    print(m, end = "", file = out_file)


def obwod_kola(r_sad: float, r: float) -> None:
    print(f"Obwod sadu: {2 * math.pi * r_sad}")
    print(f"Dlugosc plotu: {2 * math.pi * r}")


def naprawde_najkrotszy_plot(x: int, y: int, r: float) -> tuple[int, int, float]:
    najmniejsze_r: float = float("inf")
    najmniejsze_x: int = -1
    najmniejsze_y: int = -1  
    for i in range(y + r, y - r - 1, -1):
        for j in range(x - r, x + r + 1): 
            if ((i - y)**2 + (j - x)**2) <= r**2:
                if najmniejszy_plot(x, y, r, i, j) < najmniejsze_r: 
                    najmniejsze_r = najmniejszy_plot(x, y, r, i, j)
                    najmniejsze_x = j
                    najmniejsze_y = i
    return najmniejsze_x, najmniejsze_y, najmniejsze_r


def main() -> None:
    print("Podaj wymiary sadu w kolejnosci x, y, promien:")
    x_sad: int = int(input())
    y_sad: int = int(input())
    r_sad: int = int(input())
    wypisz_kolo(x_sad, y_sad, r_sad)
    print("Podaj wspolrzedne srodka plotu (x,y):")
    x: int = int(input())
    y: int = int(input())
    r = najmniejszy_plot(x_sad, y_sad, r_sad, x, y)
    zapisz_do_pliku("output.txt", x_sad, y_sad, r_sad)
    print(f"Najmniejszy plot zawieracy wszystkie drzewka: ", end = "")
    wypisz_kolo(x, y, r)
    obwod_kola(r_sad, r)
    x_min: int
    y_min: int
    r_min: float
    x_min, y_min, r_min = naprawde_najkrotszy_plot(x_sad, y_sad, r_sad)
    print("Naprawde najmniejszy plot zawieracy wszystkie drzewka:")
    wypisz_kolo(x_min, y_min, r_min)


if __name__ == "__main__":
    main()
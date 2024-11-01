import random 

random.seed(1354)


def rzucaj(liczba_kosci: int, ruch_gracza_1: bool, suma_gracza_1: int, suma_gracza_2: int) -> int:
    suma_kosci: int = 0
    with open("output.txt", "a") as plik_wynikowy: 
        if ruch_gracza_1: 
            print(f"Gracz 1 liczba kości: {liczba_kosci} wyrzucone: ", end = "", file = plik_wynikowy)
        else:
            print(f"Gracz 2 liczba kości: {liczba_kosci} wyrzucone: ", end = "", file = plik_wynikowy)
        for i in range(liczba_kosci): 
            aktualna_liczba_oczek = random.randint(1,6)
            print(aktualna_liczba_oczek, end = " ", file = plik_wynikowy)
            print(f"Wyrzuciłeś {aktualna_liczba_oczek}")
            suma_kosci += aktualna_liczba_oczek
        if ruch_gracza_1:
            suma_gracza_1 += suma_kosci + sprawdz_bonus(suma_kosci)
            print(f" bonus: {sprawdz_bonus(suma_kosci)} suma: {suma_gracza_1}", file = plik_wynikowy)
        else: 
            suma_gracza_2 += suma_kosci + sprawdz_bonus(suma_kosci)
            print(f" bonus: {sprawdz_bonus(suma_kosci)} suma: {suma_gracza_2}", file = plik_wynikowy)
        return suma_kosci


def sprawdz_bonus(n: int) -> int: 
    liczba_dzielnikow: int = 0
    for i in range(2, n): 
        if n % i == 0: 
            liczba_dzielnikow += 1
    return liczba_dzielnikow


def main() -> None:
    liczba_wygrywajaca: int  = random.randint(10, 50)
    suma_gracza_1: int = 0
    suma_gracza_2: int = 0
    ruch_gracza_1: bool = True
    liczba_kosci: int
    suma_kosci: int
    bonus: int
    plik_wynikowy = open("output.txt", "w")
    print(f"Liczba wygrywająca: {liczba_wygrywajaca}", file = plik_wynikowy)
    plik_wynikowy.close()
    while True:
        print()
        print(f"Liczba wygrywająca: {liczba_wygrywajaca}")
        print(f"Suma gracza 1: {suma_gracza_1}\nSuma gracza 2: {suma_gracza_2}")
        if (suma_gracza_1 >= liczba_wygrywajaca or suma_gracza_2 >= liczba_wygrywajaca) and ruch_gracza_1:
            plik_wynikowy = open("output.txt", "a")
            if abs(liczba_wygrywajaca - suma_gracza_1) == abs(liczba_wygrywajaca - suma_gracza_2):
                print("REMIS!")
                print("REMIS!", file = plik_wynikowy)
            else:
                print("WYGRYWA Gracz 1!" if abs(liczba_wygrywajaca - suma_gracza_1) < abs(liczba_wygrywajaca - suma_gracza_2) else "WYGRYWA Gracz 2!")
                print("WYGRYWA Gracz 1!" if abs(liczba_wygrywajaca - suma_gracza_1) < abs(liczba_wygrywajaca - suma_gracza_2) else "WYGRYWA Gracz 2!", file = plik_wynikowy)
            plik_wynikowy.close()
            break
        if ruch_gracza_1: 
            print("Ruch gracza 1.")
        else:
            print("Ruch gracza 2.")
        liczba_kosci = int(input("Iloma kośćmi chcesz rzucić?\n"))
        suma_kosci = rzucaj(liczba_kosci, ruch_gracza_1, suma_gracza_1, suma_gracza_2)
        bonus = sprawdz_bonus(suma_kosci)
        print(f"Bonus: {bonus}")
        if ruch_gracza_1:
            suma_gracza_1 += suma_kosci + sprawdz_bonus(suma_kosci)
        else:
            suma_gracza_2 += suma_kosci + sprawdz_bonus(suma_kosci)
        ruch_gracza_1 = not ruch_gracza_1
        

if __name__ == "__main__":
    main()
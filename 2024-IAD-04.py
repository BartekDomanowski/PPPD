import random

random.seed(24102024)

def wyswietl_menu() -> None: 
    print("Możliwe zadania:\n1 - dodawanie\n2 - odejmowanie\n3 - mnożenie\n4 - dzielenie z resztą (modulo)")


def dodawanie() -> int: 
    a: int = random.randint(-250,250)
    b: int = random.randint(-250,240)
    print("Wykonaj działanie: ",end="")
    if b < 0:
        print(f"{a} + ({b})")
    else: 
        print(f"{a} + {b}")
    return a + b


def odejmowanie() -> int: 
    a: int = random.randint(-145,360)
    b: int = random.randint(-300,570)
    print("Wykonaj działanie: ",end="")
    if b < 0:
        print(f"{a} - ({b})")
    else: 
        print(f"{a} - {b}")
    return a - b


def mnozenie() -> float: 
    a: int = random.randint(-100,25)
    b: int = random.random()
    b = round(b,2)
    print("Wykonaj działanie: ",end="")
    if b < 0:
        print(f"{a} * ({b})")
    else: 
        print(f"{a} * {b}")
    return a * b


def dzielenie_modulo() -> int: 
    a: int = random.randint(-25,10)
    b: int = random.randint(-15,60)
    print("Wykonaj działanie: ",end="")
    if b < 0:
        print(f"{a} % ({b})")
    else: 
        print(f"{a} % {b}")
    return a % b


def sprawdz_odpowiedz(wynik: int, wynik_uzytkownik: int, pkt_obecne: int) -> int:
    if wynik == wynik_uzytkownik: 
        print("Poprawna odpowiedź - otrzymujesz 20 pkt.")
        return pkt_obecne + 20
    else: 
        print("Niepoprawna odpowiedź - tracisz 15 pkt.")
        return pkt_obecne - 15


def main() -> None: 
    punkty_gracza: int = 100 #startowe
    imie: str = input("Witaj graczu! Podaj swoje imię (nazwa użytkownika): ")
    ile_po_kolei: int = 0
    jakie_ostatnie_zadanie: int = -1 
    wybor_uzytkownika: int
    wynik_uzytkownika: float
    while punkty_gracza > 0 and punkty_gracza < 200:
        wyswietl_menu()
        wybor_uzytkownika = int(input("Proszę wybrać rodzaj zadania: "))
        if not(wybor_uzytkownika == 1 or wybor_uzytkownika == 2 or wybor_uzytkownika == 3 or wybor_uzytkownika == 4): 
            raise ValueError("Błędne dane")

        if wybor_uzytkownika == 1: 
            if jakie_ostatnie_zadanie == 1: 
                ile_po_kolei += 1
            else:
                ile_po_kolei = 1
                jakie_ostatnie_zadanie = 1
            if ile_po_kolei < 3:
                wynik = dodawanie()
        elif wybor_uzytkownika == 2: 
            if jakie_ostatnie_zadanie == 2: 
                ile_po_kolei += 1
            else:
                ile_po_kolei = 1
                jakie_ostatnie_zadanie = 2
            if ile_po_kolei < 3:
                wynik = odejmowanie()
        elif wybor_uzytkownika == 3:
            if jakie_ostatnie_zadanie == 3: 
                ile_po_kolei += 1
            else:
                ile_po_kolei = 1
                jakie_ostatnie_zadanie = 3
            if ile_po_kolei < 3:
                wynik = mnozenie()
        else:
            if jakie_ostatnie_zadanie == 4: 
                ile_po_kolei += 1
            else:
                ile_po_kolei = 1
                jakie_ostatnie_zadanie = 4
            if ile_po_kolei < 3:
                wynik = dzielenie_modulo()

        if ile_po_kolei >= 3:
            print("Przekroczono limit 2 kolejnych pytań z tej samej kategorii - tracisz 15 pkt!")
            punkty_gracza -= 15
        else:
            wynik_uzytkownika = float(input("Podaj wynik działania: "))
            punkty_gracza = sprawdz_odpowiedz(wynik, wynik_uzytkownika, punkty_gracza)
        
        print(f"Posiadasz obecnie {punkty_gracza} pkt.")
    if punkty_gracza >= 200: 
        print(f"KONIEC GRY: Wygrałeś! {imie}, gratulujemy wygranej!")
    else: 
        print(f"KONIEC GRY: Przegrałeś! {imie}, spróbuj ponownie.")


if __name__ == "__main__": 
    main()

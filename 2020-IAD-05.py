import random
import math

random.seed(2020)

def skok(atakuje_pierwsza: bool) -> int:
    random_number: int = random.randint(1,10)
    if atakuje_pierwsza:
        if random_number <= 5:
            return 1, 0
        elif random_number <= 8:
            return 2, 0
        else:
            return 3, 0
    else:
        if random_number <= 5:
            return 0, 1
        elif random_number <= 8:
            return 0, 2
        else:
            return 0, 3
    
    
def mega_skok(atakuje_pierwsza: bool) -> int:
    random_number: int = random.randint(1,10)
    if atakuje_pierwsza: 
        if random_number <= 3:
            return 5, 0
        else:
            return -1, 0
    else:
        if random_number <= 3:
            return 0, 5
        else:
            return 0, -1
    

def atak(pozycja_pierwszej_kozicy: int, pozycja_drugiej_kozicy: int, atakuje_pierwsza: bool) -> tuple[int, int]:
    random_number: int = random.randint(1,10)
    if atakuje_pierwsza and pozycja_pierwszej_kozicy > pozycja_drugiej_kozicy:
        if random_number <= 5:
            return 0, -math.ceil(((pozycja_pierwszej_kozicy-pozycja_drugiej_kozicy) / 2) ** 2)
        else:
            return -1, 0
    elif atakuje_pierwsza == False and pozycja_drugiej_kozicy > pozycja_pierwszej_kozicy:
        if random_number <= 5:
            return -math.ceil(((pozycja_pierwszej_kozicy-pozycja_drugiej_kozicy) / 2) ** 2), 0
        else:
            return 0, -1
    else:
        return 0, 0
    

def menu() -> None:
    print("Co chcesz zrobić?\n1 - skok\n2 - mega skok\n3 - atak")


def main() -> None:
    pozycja_pierwszej_kozicy: int = 0
    pozycja_drugiej_kozicy: int = 0 
    atakuje_pierwsza: bool = True
    zmiana_pola_pierwszej: int
    zmiana_pola_drugiej: int
    akcja_uzytkownika: int
    while pozycja_pierwszej_kozicy < 20 and pozycja_drugiej_kozicy < 20:
        if atakuje_pierwsza:
            print("Ruch kozicy 1.")
        else:
            print("Ruch kozicy 2.")
        menu()
        akcja_uzytkownika = int(input())
        if akcja_uzytkownika < 1 or akcja_uzytkownika > 3:
            raise ValueError("Podana akcja powinna być liczbą z przedzialu 1-3!")
        if akcja_uzytkownika == 1:
            zmiana_pola_pierwszej, zmiana_pola_drugiej = skok(atakuje_pierwsza)
            print(f"Długość skoku: {max(zmiana_pola_pierwszej, zmiana_pola_drugiej)}.")
        elif akcja_uzytkownika == 2: 
            zmiana_pola_pierwszej, zmiana_pola_drugiej = mega_skok(atakuje_pierwsza)
            if zmiana_pola_pierwszej == 5 or zmiana_pola_drugiej == 5:
                print("Kozica wykonała mega skok!")
            else:
                print("Mega skok się nie udał, kozica cofa się o 1 pole.")
        else:
            zmiana_pola_pierwszej, zmiana_pola_drugiej = atak(pozycja_pierwszej_kozicy, pozycja_drugiej_kozicy, atakuje_pierwsza)
            if zmiana_pola_pierwszej == zmiana_pola_drugiej == 0:
                print("Strata ruchu, kozica, która jest niżej nie może atakować!")
            elif zmiana_pola_pierwszej == -1 or zmiana_pola_drugiej == -1: 
                print("Atak się nie udał, atakująca kozica cofa się o 1 pole.")
            else:
                print(f"Atak się powiódł, atakowana kozica cofa się o {(-1) * min(zmiana_pola_pierwszej, zmiana_pola_drugiej)} pola.")

        pozycja_pierwszej_kozicy += zmiana_pola_pierwszej
        pozycja_pierwszej_kozicy = max(0, pozycja_pierwszej_kozicy)

        pozycja_drugiej_kozicy += zmiana_pola_drugiej
        pozycja_drugiej_kozicy = max(0, pozycja_drugiej_kozicy)

        print(f"Pozycja kozicy 1: {pozycja_pierwszej_kozicy}\nPozycja kozicy 2: {pozycja_drugiej_kozicy}")
        atakuje_pierwsza = not atakuje_pierwsza
        if pozycja_pierwszej_kozicy >= 20 or pozycja_drugiej_kozicy >= 20:
            if pozycja_pierwszej_kozicy == pozycja_drugiej_kozicy: 
                print("REMIS!")
            else:
                print("WYGRYWA kozica 2!" if pozycja_drugiej_kozicy > pozycja_pierwszej_kozicy else "WYGRYWA kozica 1!")


if __name__ == "__main__":
    main()
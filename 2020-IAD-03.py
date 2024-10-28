#Funcja przyjmuje liczbe naturalna n i wypisuje wszystkie dzielniki pierwsze bez powtórzeń
def wypisz_dzielniki_pierwsze(n: int) -> None:
    dzielnik_pierwszy: int = 2
    while n > 1:
        czy_aktualny_dzielnik_wykorzystany = False
        while n % dzielnik_pierwszy == 0: 
            czy_aktualny_dzielnik_wykorzystany = True
            n /= dzielnik_pierwszy
        if czy_aktualny_dzielnik_wykorzystany: 
            print(dzielnik_pierwszy)
        dzielnik_pierwszy += 1


#Funcja przyjmuje liczbe naturalna n i zwraca dzielnik pierwszy o największej krotność oraz samą krotność
def znajdz_dzielniki_o_max_krotnosci(n: int) -> tuple[int, int]:
    dzielnik_pierwszy: int = 2
    max_dzielnik: int = -1
    max_krotnosc: int = -1
    while n > 1:
        krotnosc_aktualnego_dzielnika = 0
        while n % dzielnik_pierwszy == 0: 
            krotnosc_aktualnego_dzielnika += 1
            n /= dzielnik_pierwszy
        if krotnosc_aktualnego_dzielnika > max_krotnosc: 
            max_krotnosc = krotnosc_aktualnego_dzielnika
            max_dzielnik = dzielnik_pierwszy
        dzielnik_pierwszy += 1
    return max_dzielnik, max_krotnosc


#Funcja przyjmuje liczbe naturalna n i wypisuje jaka liczbę byśmy otrzymali pomijając krotność czynników pierwszych
def liczba_bez_krotnosci(n: int) -> int:
    dzielnik_pierwszy: int = 2
    wynik: int = 1
    while n > 1:
        czy_aktualny_dzielnik_wykorzystany = False
        while n % dzielnik_pierwszy == 0: 
            czy_aktualny_dzielnik_wykorzystany = True
            n /= dzielnik_pierwszy
        if czy_aktualny_dzielnik_wykorzystany: 
            wynik *= dzielnik_pierwszy
        dzielnik_pierwszy += 1
    return wynik


def main() -> None: 
    n: float = float(input("Podaj liczbe naturalna n: "))
    #Sprawdzanie poprawności danych
    if n < 1: 
        raise ValueError("Błędne dane!")
    elif int(n) - float(n) != 0: 
        raise ValueError("Błędne dane!")
    
    n: int = int(n)
    #1.
    wypisz_dzielniki_pierwsze(n)

    #2.
    wynik_2: tuple[int, int] = znajdz_dzielniki_o_max_krotnosci(n)
    print(f"W rozkladzie {n} na czynniki pierwsze najczęściej pojawia się {wynik_2[0]}, występuje {wynik_2[1]} razy.")
    
    #3.
    print(f"Jeżeli w rozkładzie {n} na czynniki pierwsze pominiemy krotności, otrzymamy liczbę {liczba_bez_krotnosci(n)}.")


if __name__ == "__main__": 
    main()
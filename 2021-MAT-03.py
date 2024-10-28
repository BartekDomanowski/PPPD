def menu() -> None: 
    print("Co chcesz zrobić?\n0 - Sprawdzić czy dwie liczby są lustrzane\n1 - Zakończyć")


def ile_cyfr_w_liczbie(n: int) -> int:
    odp: int = 0
    while n > 0: 
        odp += 1
        n //= 10
    return odp


def odwroc_cyfre(n: int) -> int:
    odwrocona: int = 0
    while n > 0:
        odwrocona += (n % 10)
        odwrocona *= 10
        n //= 10
    return odwrocona / 10 


def czy_lustrzane(a: int, b: int) -> bool:
    return a == odwroc_cyfre(b)


def main() -> None: 
    while True: 
        menu()
        wybor_uzytkownika: int = int(input())
        while not(wybor_uzytkownika == 0 or wybor_uzytkownika == 1):
            print("Błędny wybór. Spróbuj jeszcze raz.")
            menu()
            wybor_uzytkownika: int = int(input())
        if wybor_uzytkownika == 1:
            break
        
        liczba_1: int = int(input("Podaj pierwszą liczbę\n"))
        if liczba_1 < 1 or liczba_1 >= 10**10:
            raise ValueError("Liczby muszą być dodatnie i mniejsze od 10ˆ10")
        
        liczba_2: int = int(input("Podaj drugą liczbę\n"))
        if liczba_2 < 1 or liczba_2 >= 10**10:
            raise ValueError("Liczby muszą być dodatnie i mniejsze od 10ˆ10")
        
        if ile_cyfr_w_liczbie(liczba_1) != ile_cyfr_w_liczbie(liczba_2):
            print("Liczby mają różną liczbę cyfr.\nNie mogą to być liczby lustrzane.")
            break
        else:
            print("Liczby mają taką samą liczbę cyfr.")

        if czy_lustrzane(liczba_1, liczba_2):
            print("Podane liczby SĄ liczbami lustrzanymi.")
        else:
            print("Nie mogą to być liczby lustrzane.")


if __name__ == "__main__":
    main()
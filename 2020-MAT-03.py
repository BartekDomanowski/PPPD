#Funkcja pobiera liczbę n i zwraca liczbę n bez 0 w zapisie dziesiętnym 
def usun_zera(n: int) -> int: 
    wynik: int = 0
    potega_10: int = 1
    while n > 0: 
        if n % 10 != 0:
            wynik = potega_10 * (n % 10) + wynik
            potega_10 *= 10
        n //= 10 
    return wynik 


#Funkcja przyjmuje liczbę n i zwrca iloczyn cyrf tej liczby
def pomznoz_cyfry(n: int) -> int: 
    wynik: int = 1
    while n > 0:
        wynik *= (n % 10)
        n //= 10 
    return wynik


#Fukncja liczy indeks numerologiczny określony w zadaniu oraz niezbędną do tego liczbę kroków
def ind(n: int, kroki: int) -> tuple[int, int]:
    if n < 10: 
        return (n, kroki)
    m: int = pomznoz_cyfry(usun_zera(n))
    return ind(m, kroki + 1)


def main() -> None: 
    n: int = int(input("Podaj liczbę naturalną n: "))
    if n < 1: 
        raise ValueError("Błędne dane!")
    
    #1. 
    print(f"Po pominięciu wszystkich zer w zapisie dziesiętnym liczby {n} otrzymamy liczbę {usun_zera(n)}.")
    
    #2. 
    indeks: int
    kroki: int
    indeks, kroki = ind(n, 0)
    print(f"Indeks numerologiczny liczby {n} wynosi {indeks}.")
    print(f"Jesteśmy w stanie go obliczyć w {kroki} krokach.")

if __name__ == "__main__": 
    main()
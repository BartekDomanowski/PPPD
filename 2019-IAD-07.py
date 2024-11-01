def podaj(podpis_zbioru: str) -> list[int]:
    rozmiar: int = int(input(f"Podaj rozmiar zbioru {podpis_zbioru}\n"))
    print(f"Podaj elementy zbioru {podpis_zbioru}:")
    zbior: list[int] = [0] * rozmiar
    for i in range(rozmiar):
        aktualny_element = int(input(f"Podaj ilość {i}: "))
        if i == rozmiar - 1 and aktualny_element == 0: 
            raise ValueError("Niepoprawne dane, ostatni indeks nie moze byc zerowy!")
        zbior[i] = aktualny_element
    return zbior


def wypisz(lista: list[int]) -> list[int]:
    wynik: list[int] = []
    i = 0
    for licznosc in lista: 
        wynik += [i] * licznosc
        i += 1
    return wynik


def dodaj(zbior: list[int], element: int) -> list[int]: 
    if element < len(zbior):
        zbior[element] += 1
        return zbior
    else:
        rozmiar: int = element
        nowy_zbior: list[int] = [0] * (rozmiar + 1)
        for i in range(rozmiar + 1):
            if i < len(zbior):
                nowy_zbior[i] = zbior[i]
            else:
                if i == rozmiar:
                    nowy_zbior[i] = 1
                else:
                    nowy_zbior[i] = 0
        return nowy_zbior
    

def przeciecie(zbiorA: list[int], zbiorB: list[int]) -> list[int]:
    ostatnia_indeks_wspolny: int = -1
    ostatni_indeks: int = min(len(zbiorA), len(zbiorB))
    for i in range(ostatni_indeks - 1, 0, -1):
        if zbiorA[i] > 0 and zbiorB[i] > 0:
            ostatnia_indeks_wspolny = i
            break
    if ostatnia_indeks_wspolny == -1: 
        return []
    lista_przeciecia: list[int] = [0] * (ostatnia_indeks_wspolny + 1)
    for i in range(ostatnia_indeks_wspolny + 1):
        lista_przeciecia[i] = min(zbiorA[i], zbiorB[i])
    return lista_przeciecia


def roznica(zbiorA: list[int], zbiorB: list[int]) -> list[int]:
    zbior_roznicy: list[int] = [0] * len(zbiorA)
    for i in range(len(zbiorA)): 
        if i >= len(zbiorB): 
            zbior_roznicy[i] = zbiorA[i]
        elif zbiorA[i] > zbiorB[i]: 
            zbior_roznicy[i] = zbiorA[i] - zbiorB[i]
        else: 
            zbior_roznicy[i] = 0
    return zbior_roznicy
    

def main() -> None:
    zbiorA: list[int] = podaj("A")
    print("Podany zbiór to:\n", wypisz(zbiorA), sep = "")
    nowy_element: int = int(input("Podaj nowy element zbioru A\n"))
    zbiorA = dodaj(zbiorA, nowy_element)
    print(wypisz(zbiorA))
    zbiorB: list[int] = podaj("B")
    print("Roznica zbiorow:\n",wypisz(roznica(zbiorA, zbiorB)), sep = "")
    print("Przeciecie zbiorow:\n",wypisz(przeciecie(zbiorA, zbiorB)), sep = "")
    # TUTAJ TESTY POSZEGÓLNYCH FUNKCJI 
    # print(przeciecie([0,3,0,4,0,1], [1,2,2,4,1]))
    # print(przeciecie([0,3,0,4], [1,0,2,0]))
    # print(roznica([0,3,0,4], [1,2,2,4]))
    # print(roznica([1,2], [2,1]))
    # print(dodaj([0,2], 5))
    # print(roznica([0,3,0,4,0,1], [1,2,2,4,1]))

if __name__ == "__main__": 
    main()
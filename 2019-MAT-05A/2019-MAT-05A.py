import random


def mozliwe_akcje() -> None: 
    print("1 - atak toporem(230 obrazen, 30 % szan na trafienie)")
    print("2 - magiczny pocisk(50 - 100 obrazen, 20 punktow many")
    print("3 - potezny atak(200 - 400 obrazen, 35 % szans na trafienie, raz na cztery tury)")
    print("4 - zapisz grę")
    print("5 - odczytaj grę")


def wypisz_zycie_trolla(zycie_trolla: int) -> None: 
     print(f"Troll ma {zycie_trolla} pkt. życia")


def pobierz_akcje(mana_zygfryda: int, tura_3: int) -> int: 
    mozliwe_akcje()
    while True: 
        akcja_uzytkownika: int = int(input("Wybierz akcję: "))
        if akcja_uzytkownika < 1 or akcja_uzytkownika > 5:
            print("Numer akcji musi być pomiędzy 1 a 5")
        elif akcja_uzytkownika == 2 and mana_zygfryda < 20:
            print("Za mało many.")
            akcja_uzytkownika = -1
        elif akcja_uzytkownika == 3 and tura_3 >= 1: 
            print("Jeszcze za wcześnie na atak 3")
            akcja_uzytkownika = -1
        else:
            break
    if akcja_uzytkownika == 1: 
        return 1
    elif akcja_uzytkownika == 2: 
        return 2
    elif akcja_uzytkownika == 3: 
        return 3
    elif akcja_uzytkownika == 4: 
        return 4
    else: 
        return 5
    

def zapisz_gre(zycie_trolla: int, mana_zygfryda: int, tura_3: int) -> None:
    sciezka: str = input("Podaj ścieżkę do pliku, gdzie ma być zapisana gra: ")
    with open(sciezka, "w") as out_file: 
        print(f"{zycie_trolla}\n{mana_zygfryda}\n{tura_3}", file = out_file)


def odczytaj_gre() -> tuple[int, int, int]: 
    sciezka: str = input("Podaj ścieżkę do pliku, gdzie jest zapisana gra: ")
    with open(sciezka, "r") as in_file: 
        zycie_trolla: int = int(in_file.readline())
        mana_zygfryda: int = int(in_file.readline())
        tura_3: int = int(in_file.readline())
    return zycie_trolla, mana_zygfryda, tura_3


def main() -> None: 
    random.seed(2137)
    zycie_trolla: int = 1000
    mana_zygfryda: int = 100
    tura_3: int = 0
    while zycie_trolla > 0: 
        wypisz_zycie_trolla(zycie_trolla)
        akcja_uzytkownika: int = pobierz_akcje(mana_zygfryda, tura_3)
        if akcja_uzytkownika == 1: 
            liczba: float = random.random()
            if liczba <= 0.3: 
                zycie_trolla -= 230
            if tura_3 > 0: 
                tura_3 += 1
                tura_3 %= 4
        elif akcja_uzytkownika == 2: 
            liczba: int = random.randint(50, 100)
            zycie_trolla -= liczba
            mana_zygfryda -= 20
            if tura_3 > 0: 
                tura_3 += 1
                tura_3 %= 4
        elif akcja_uzytkownika == 3: 
            tura_3 = 1
            liczba_do_obrazen: int = random.randint(200, 400)
            liczba_do_trafienia: float = random.random()
            if liczba_do_trafienia <= 0.35:
                zycie_trolla -= liczba_do_obrazen
        elif akcja_uzytkownika == 4: 
            zapisz_gre(zycie_trolla, mana_zygfryda, tura_3)
        else: 
            zycie_trolla, mana_zygfryda, tura_3 = odczytaj_gre()


if __name__ == "__main__": 
    main()
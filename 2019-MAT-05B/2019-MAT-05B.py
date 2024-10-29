import random


def mozliwe_akcje() -> None: 
    print("Mozliwe akcje:") 
    print("1 - walka")
    print("2 - ucieczka")
    print("3 - cios kung-fu")
    print("4 - zapisz gre")
    print("5 - wczytaj gre")


def wypisz_zycie(hp_fryderyka: int) -> None: 
    print(f"Masz jeszcze {hp_fryderyka} punktow zycia")


def pobierz_akcje(ile_3_z_kolei: int, hp_goblina: int) -> int:
    while True:
        numer_akcji: int = int(input("Wybierz akcje: "))
        if numer_akcji < 1 or numer_akcji > 5: 
            print("Numer akcji powinien byc z przedzialu 1 - 5")
        elif numer_akcji == 3 and ile_3_z_kolei > 0:
            print("Jeszcze nie mozesz uzyc ciosu kung-fu!")
        elif numer_akcji == 2 and hp_goblina < 100: 
            print("Ucieczka bylaby ponizajaca, zrob cos innego!")
        else: 
            return numer_akcji
        

def zapisz_gre(hp_fryderyka: int, zloto_fryderyka: int, ile_3_z_kolei: int) -> None:
    sciezka: str = input("Podaj ścieżkę do pliku, gdzie ma być zapisana gra: ")
    with open(sciezka, "w") as out_file: 
        print(f"{hp_fryderyka}\n{zloto_fryderyka}\n{ile_3_z_kolei}", file = out_file)


def odczytaj_gre() -> tuple[int, int, int]: 
    sciezka: str = input("Podaj ścieżkę do pliku, gdzie jest zapisana gra: ")
    with open(sciezka, "r") as in_file: 
        hp_fryderyka: int = int(in_file.readline())
        zloto_fryderyka: int = int(in_file.readline())
        ile_3_z_kolei: int = int(in_file.readline())
    return hp_fryderyka, zloto_fryderyka, ile_3_z_kolei


def main() -> None: 
    random.seed(2137)
    hp_fryderyka: int = 500 
    ile_3_z_kolei: int = 0
    zloto_fryderyka: int = 0
    while hp_fryderyka > 0: 
        print()
        wypisz_zycie(hp_fryderyka)
        sila_losowego_straznika: int = random.randint(0, 200)
        ilosc_zlota_straznika: int = random.randint(0, 200)
        print(f"Goblin o sile {sila_losowego_straznika} broni {ilosc_zlota_straznika} sztuk zlota")
        numer_akcji: int = pobierz_akcje(ile_3_z_kolei, sila_losowego_straznika)
        if numer_akcji == 1: 
            obrazenia_straznika = random.randint(0, sila_losowego_straznika)
            hp_fryderyka -= obrazenia_straznika 
            if hp_fryderyka > 0: 
                zloto_fryderyka += ilosc_zlota_straznika
            if ile_3_z_kolei > 0:
                ile_3_z_kolei += 1
                ile_3_z_kolei %= 4
        elif numer_akcji == 2: 
            szansa_ze_straznik_dogoni: int = random.randint(1,10)
            if szansa_ze_straznik_dogoni <= 2: 
                obrazenia_straznika = random.randint(0, 2 * sila_losowego_straznika)
                hp_fryderyka -= sila_losowego_straznika
            if ile_3_z_kolei > 0:
                ile_3_z_kolei += 1
                ile_3_z_kolei %= 4
        elif numer_akcji == 3: 
            ile_3_z_kolei = 1
            zloto_fryderyka += ilosc_zlota_straznika
        elif numer_akcji == 4: 
            zapisz_gre(hp_fryderyka, zloto_fryderyka, ile_3_z_kolei)
        else:
            hp_fryderyka, zloto_fryderyka, ile_3_z_kolei = odczytaj_gre()
    print(f"Giniesz. Zebrales {zloto_fryderyka} sztuk zlota.")


if __name__ == "__main__":
    main()
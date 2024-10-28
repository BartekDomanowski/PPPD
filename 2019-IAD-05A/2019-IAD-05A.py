import random 

random.seed(2137)

def drzewo(x: int , y: int) -> bool:
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


def wypisz_prostokat(x_min: int, x_max: int, y_min: int, y_max: int) -> None:
    print(f"[{x_min}, {x_max}]x[{y_min}, {y_max}]")


def najmniejszy_plot(x_min: int, x_max: int, y_min: int, y_max: int) -> tuple[int, int, int, int]:
    najmniejszy_x: int
    najmniejszy_y: int
    najwiekszy_x: int
    najwiekszy_x: int
    najmniejszy_x, najmniejszy_y = float("inf"), float("inf") 
    najwiekszy_x, najwiekszy_y = -float("inf"), -float("inf")
    cnt = 0 
    for i in range(y_max, y_min - 1, -1): 
        for j in range(x_min, x_max + 1):
            if drzewo(i, j): 
                cnt += 1
                najmniejszy_x = min(i, najmniejszy_x)   
                najmniejszy_y = min(j, najmniejszy_y)
                najwiekszy_x = max(i, najwiekszy_x)
                najwiekszy_y = max(j, najwiekszy_y)
    if cnt == 0:
        return 0, 0, 0, 0
    return najmniejszy_x, najwiekszy_x, najmniejszy_y, najwiekszy_y


def obwod_prostokata(x_min: int, x_max: int, y_min: int, y_max: int) -> int: 
    return 2*(x_max - x_min) + 2*(y_max - y_min) 


def zapisz_do_pliku(sciezka: str, x_min: int, x_max: int, y_min: int, y_max: int) -> None:
    with open(sciezka, "w") as out_file: 
        for i in range(y_max, y_min - 1, -1):
            print(f"{i:<5}", end = "", file = out_file)  
            for j in range(x_min, x_max + 1):
                if drzewo(i, j): 
                    print("D", end = "", file = out_file)
                else: 
                    print(".", end = "", file = out_file)
            print(file = out_file)
            if i == y_min: 
                print(f"y/x  ", end = "", file = out_file)
                for x in range(x_min, x_max + 1): 
                    print(x, end = "", file = out_file)


def najlepszy_podzial(x_min: int, x_max: int, y_min: int, y_max: int) -> int:
    najmniejszy_obwod: float = float("inf")
    dla_jakiego_x_obwod: int = -1
    for i in range(x_min, x_max + 1):
        curr_x_min1: int
        curr_x_max1: int
        curr_y_min1: int
        curr_y_max1: int
        curr_x_min1, curr_x_max1, curr_y_min1, curr_y_max1 = najmniejszy_plot(x_min, i, y_min, y_max)
        obwod_1: int = obwod_prostokata(curr_x_min1, curr_x_max1, curr_y_min1, curr_y_max1)
        obwod_2: int = 0 
        if i + 1 <= x_max:
            curr_x_min2: int
            curr_x_max2: int
            curr_y_min2: int
            curr_y_max2: int
            curr_x_min2, curr_x_max2, curr_y_min2, curr_y_max2 = najmniejszy_plot(i + 1, x_max, y_min, y_max)
            obwod_2 = obwod_prostokata(curr_x_min2, curr_x_max2, curr_y_min2, curr_y_max2)
        obwod_laczny: int = obwod_1 + obwod_2
        if obwod_laczny < najmniejszy_obwod: 
            najmniejszy_obwod = obwod_laczny
            dla_jakiego_x_obwod = i
        #print(f"Podzial dla x = {i}, obwod 1 = {obwod_1}, obwod 2 = {obwod_2}, razem = {obwod_laczny}")
    return dla_jakiego_x_obwod


def main() -> None:
    print("Podaj wymiary sadu w kolejnosci xmin, xmax, ymin, ymax:")
    x_min: int = int(input())
    x_max: int = int(input())
    y_min: int = int(input())
    y_max: int = int(input())
    print("Podany prostokąt to:")
    wypisz_prostokat(x_min, x_max, y_min, y_max)
    najmniejszy_x: int
    najmniejszy_y: int
    najwiekszy_x: int
    najwiekszy_x: int
    najmniejszy_x, najwiekszy_x, najmniejszy_y, najwiekszy_y = najmniejszy_plot(x_min, x_max, y_min, y_max)
    zapisz_do_pliku("output.txt", x_min, x_max, y_min, y_max)
    print(f"Obwód sadu: {obwod_prostokata(x_min, x_max, y_min, y_max)}")
    print(f"Obwód płotu: {obwod_prostokata(najmniejszy_x, najwiekszy_x, najmniejszy_y, najwiekszy_y)}")
    print(f"Najlepszy podział to: {najlepszy_podzial(x_min, x_max, y_min, y_max)}")


if __name__ == "__main__": 
    main()
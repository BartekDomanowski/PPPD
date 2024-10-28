def main() -> None: 
    height: int = int(input("Podaj wysokość ściany {7, 9, 11}: "))
    width: int = 10
    if not(height == 7 or height == 9 or height == 11):
        raise ValueError("Niepoprawna wysokość ściany")
    x_length: int = int(input("Podaj długość rolki `x`: "))
    o_length: int = int(input("Podaj długość rolki `o`: "))

    if o_length * 2 > x_length or x_length > width - 1 or x_length <= 0 or o_length <=0: 
        raise ValueError("Nieprawidłowe wartości długości rolek `o` i `x`")
    
    x_time: float = float(input("Podaj czas klejenia jednej jednostki z rolki `x`: "))
    o_time: float = x_time / 3
    change_time: float  = x_time * 3
    print(f"Czas klejenia x= {x_time}, czas klejenia o={o_time}, czas zmiany rolki= {change_time}")
    window_width = 3
    window_height = 3

    x_left: int = x_length
    o_left: int = o_length
    o_now: bool = True #Zaczynam od rolki 'o' więc teraz będzie 'o'
    cnt_x_tape: int = 0 
    cnt_o_tape: int = 0
    time_to_tape: float = change_time # czas potrzebny do załozenia rolki
    for i in range(height): 
        for j in range(width): 
            #Czy tu jest okno? 
            if (i == height - 3 or i == height - 4 or i == height - 5) and (j == width - 3 or j == width - 4 or j == width - 5):
                print(" ",end="")
                continue
            #Skończyła się taśma 'o' i zmieniam ją na 'x'
            if o_left == 0:
                time_to_tape += change_time 
                o_left = o_length
                o_now = False
            elif x_left == 0: #Skończyła się taśma 'x' i zmieniam ją na 'o'
                time_to_tape += change_time
                x_left = x_length
                o_now = True
            if o_now: #Teraz jest taśma 'o' zatem wypisuje 'o' i zmieniam czasy i ew. ilość zuytych rolek
                if o_left == o_length: 
                    cnt_o_tape += 1
                time_to_tape += o_time
                print("o",end="")
                o_left -= 1
            else: #Teraz jest taśma 'x' zatem wypisuje 'x' i zmieniam czasy i ew. ilość zuytych rolek
                if x_left == x_length: 
                    cnt_x_tape += 1
                time_to_tape += x_time
                print("x",end="")
                x_left -= 1
        print()
    print(f"Wytapetowanie całego pokoju zajeło {time_to_tape} jednostek czasu")
    print(f"Podczas tapetowania zużyto: {cnt_x_tape} rolek x i {cnt_o_tape} rolek tapety o")
if __name__ == '__main__':
    main()
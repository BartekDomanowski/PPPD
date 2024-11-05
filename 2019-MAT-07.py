def policz_kolejny_wiersz(wiersz, i):
    kolejny_wiersz = [0] * (len(wiersz) + 2)
    kolejny_wiersz[0] = wiersz[0]
    kolejny_wiersz[len(kolejny_wiersz) - 1] = wiersz[len(wiersz) - 1] 
    for i in range(1, len(kolejny_wiersz) - 1): 
        if i == 1: 
            kolejny_wiersz[i] = wiersz[i - 1] + wiersz[i]
        elif i == (len(kolejny_wiersz) - 2): 
            kolejny_wiersz[i] = wiersz[i - 1] + wiersz[i - 2]
        else: 
            kolejny_wiersz[i] = wiersz[i - 2] + wiersz[i - 1] + wiersz[i]
    return kolejny_wiersz


# wiersz: 
# 0 1 2
# 1 1 1
# kolejny_wiersz
# 0 1 2 3 4
# 1 2 3 2 1


def trojkat(a, b, c, d, n): 
    if n < 1: 
        raise ValueError("zle")


    if n == 1: 
        return [a]
    elif n == 2: 
        return [b, c, d]
    else: 
        aktualny_wiersz = [b, c, d]
        numer_aktualnego_wiersza = 2
        for i in range(3, n + 1): 
            kolejny_wiersz = policz_kolejny_wiersz(aktualny_wiersz, numer_aktualnego_wiersza)
            aktualny_wiersz = kolejny_wiersz
            numer_aktualnego_wiersza += 1   
    return aktualny_wiersz


def main(): 
    wiesz = trojkat(1, 1, 1, 1, 5)
    print(wiesz)


if __name__ == "__main__": 
    main()
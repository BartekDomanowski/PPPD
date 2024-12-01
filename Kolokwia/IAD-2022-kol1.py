def Zadanie1A1(n: int) -> int: 
    if n == 0 or n == 1: 
        return n
    i = 1
    Cn = 0 
    Help_tab = [0] * (n + 1)
    pointer = 0
    while i <= 2 * n: #Dokładnie O(2 * n) ogólnie to jest liniowe O(n)
        if i % 2 == 0:
            #print(Help_tab)
            if Help_tab[pointer] < i:
                #print(f"Tu odejmuje: Help_tab[{pointer}] = {Help_tab[pointer]}")
                Cn -= Help_tab[pointer]
                pointer += 1
            Help_tab[int(i / 2)] = Cn  
            #print(f"C{int(i/2)} = {Cn}")
        if i != 2 * n:
            #print(f"Do Cn dodaje {i}")
            Cn += i 
        i += 1
    return Help_tab[n]


def Zadanie1A2(n: int): 
    # 2! = 1 * 2
    # 4! = Prev * 3 * 4
    # 6! = Prev * 5 * 6 
    # itd. 
    answer = 1
    factorials = [1] * (4 * n + 1)
    powers = [1] * (6 * n + 1)
    for i in range(1, 6 * n + 1):
        if i <= 4 * n: 
            factorials[i] = factorials[i - 1] * i
        powers[i] = powers[i - 1] * (-4)
    #print(factorials, powers)
    for k in range(1, 2 * n + 1): 
        answer *= ( (factorials[2 * k] * powers[3 * k])/(k * k) )
        #print(f"skladnik {k} = {answer}")
    return answer


def ZadanieIA3(a: int, b: int) -> float: 
    if b == 1 or b == 2:
        return 1
    if b == 3: 
        return 2
    Cn_3 = 1
    Cn_2 = 1
    Cn_1 = 2
    Cn = -1
    SumToCa = 4
    SumOfAll = 4
    for n in range(4, b + 1): 
        Cn = ( ((2 * n + 1) / (n + 2)) * Cn_1 )+ ( ((3 * n - 3) / (n + 2)) * Cn_3 )
        if n < a: 
            SumToCa += Cn
        SumOfAll += Cn
        Cn_3 = Cn_2
        Cn_2 = Cn_1
        Cn_1 = Cn
        #print(f"C{n} = {Cn:.2f}")
    return SumOfAll - SumToCa



def main() -> None:
    print(Zadanie1A1(5))
    print(Zadanie1A2(1))
    print(f"{ZadanieIA3(4, 7):.2f}")



if __name__ == "__main__":
    main()
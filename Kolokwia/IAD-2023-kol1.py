def f(x): 
    return x


def suma_malych_iloczynow_2_5_pkt(n, X): 
    sum = 0
    for i in range(n + 1): 
        for j in range(n + 1): 
            if f(i) * f(j) < X: 
                sum += (f(i) * f(j))
    return sum


def suma_malych_iloczynow(n, X): 
    summ = 0
    for i in range(1, n + 1): 
        summ += f(i)
    answer = 0 
    max_j = n 
    for i in range(1, n + 1): 
        while f(i) * f(max_j) >= X and max_j >= 0: #Ta pętla łącznie wykona się maksymalnie n razy 
            summ -= f(max_j)
            max_j -= 1
        answer += summ * f(i)
    return answer


def Zadanie1A2(x, n): 
    factorials = [1] * (9 * n + 1)
    powers_3 = [1] * (3 * n + 1)
    powers_x = [1] * (9 * n + 1)
    for i in range(1, 9 * n + 1): 
        if i <= 3 * n: 
            powers_3[i] = powers_3[i - 1] * (-3)
        factorials[i] = factorials[i - 1] * i
        powers_x[i] = powers_x[i - 1] * x
    answer = 1
    #print(powers_3, powers_x, factorials)
    for i in range(3, 3 * n + 1): 
        answer *= ( powers_3[i] * powers_x[3 * i] )/ factorials[3 * i]
        #print(powers_3[i], powers_x[3 * i], factorials[3 * i])
        #print(i, answer)
    return x + answer
    # pi od 3 = -27 * 64 / 720 * 8 * 9 


def ZadanieIA3(x, y): 
    pass


def Zadanie1A4(lista1, lista2): #O (n + m)
    maxi = -float("inf")
    # n operacji
    for i in range(len(lista1)):
        if lista1[i] > maxi:
            maxi = lista1[i]
    # n operacji
    for i in range(len(lista2)):
        if lista2[i] > maxi:
            maxi = lista2[i]

    czy_wystapilo = [0] * (maxi + 1) # lista 10 komórek [0-9]
    for liczba in lista1:
        czy_wystapilo[liczba] = 1
    for liczba in lista2:
        czy_wystapilo[liczba] = 1
    dlugosc_wyniku = 0
    for i in range(len(czy_wystapilo)):
        if czy_wystapilo[i] == 1:
            dlugosc_wyniku += 1
    wynik = [0] * dlugosc_wyniku
    pointer_wynik = 0
    p1 = 0
    p2 = 0
    while p1 < len(lista1) and p2 < len(lista2):
        if lista1[p1] >= lista2[p2]:
            wynik[pointer_wynik] = lista1[p1]
            while p1 < len(lista1) and lista1[p1] == wynik[pointer_wynik]:
                p1 += 1
            #To jest w razie równości
            while p2 < len(lista2) and lista2[p2] == wynik[pointer_wynik]:
                p2 += 1
            pointer_wynik += 1
        else: #Tutaj lista2[p2] to mniej
            wynik[pointer_wynik] = lista2[p2]
            while p2 < len(lista2) and lista2[p2] == wynik[pointer_wynik]:
                p2 += 1
            pointer_wynik += 1

    while p1 == len(lista1) and p2 < len(lista2):
        wynik[pointer_wynik] = lista2[p2]
        while p2 < len(lista2) and lista2[p2] == wynik[pointer_wynik]:
            p2 += 1
        pointer_wynik += 1
    while p1 < len(lista1) and p2 == len(lista2):
        wynik[pointer_wynik] = lista1[p1]
        while p1 < len(lista1) and lista1[p1] == wynik[pointer_wynik]:
            p1 += 1
        pointer_wynik += 1
    return wynik


def main(): 
    print(suma_malych_iloczynow(3,4))
    print(Zadanie1A2(2, 1))
    l1 = [12, 10, 9, 8, 6, 3, 2, 1]
    l2 = [13, 9, 7, 5, 3]
    print(Zadanie1A4(l1, l2))


if __name__ == "__main__": 
    main()
def mozliwe_ruchy(n, pozycja):
    posibilities = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    size_of_answer = 0
    for move in posibilities: 
        new_x = pozycja[0] + move[0]
        new_y = pozycja[1] + move[1]
        if inside(n, new_x, new_y): 
            size_of_answer += 1
    answer = [[0, 0] for i in range(size_of_answer)]
    pointer = 0
    for move in posibilities: 
        new_x = pozycja[0] + move[0]
        new_y = pozycja[1] + move[1]
        if inside(n, new_x, new_y): 
            answer[pointer][0] = new_x
            answer[pointer][1] = new_y
            pointer += 1
    return answer


def inside(n, a, b): 
    return 0 <= a and a < n and 0 <= b and b < n


def pozycja_na_liczbe(n, pozycja):
    return pozycja[0] * n + pozycja[1]


def liczba_na_pozycje(n, liczba):
    return [liczba // n, liczba % n]


def macierz_przejscia(n):
    answer_matrix = [ [0 for i in range(n**2)] for i in range(n**2) ]
    for pozycja_x in range(n): 
        for pozycja_y in range(n): 
            przetlumaczona_pozycja = pozycja_na_liczbe(n, [pozycja_x, pozycja_y])
            mozliwosci_xy = mozliwe_ruchy(n, [pozycja_x, pozycja_y])
            #print(pozycja_x, pozycja_x, przetlumaczona_pozycja, mozliwosci_xy)
            if len(mozliwosci_xy) == 0: 
                answer_matrix[przetlumaczona_pozycja][przetlumaczona_pozycja] = 1
                continue
            for pozycja_x_2 in range(n): 
                for pozycja_y_2 in range(n):
                    przetlumaczona_pozycja_2 = pozycja_na_liczbe(n, [pozycja_x_2, pozycja_y_2])
                    #print(pozycja_x_2, pozycja_y_2, przetlumaczona_pozycja_2)
                    if [pozycja_x_2, pozycja_y_2] in mozliwosci_xy:
                            answer_matrix[przetlumaczona_pozycja][przetlumaczona_pozycja_2] = 1 / len(mozliwosci_xy)
    return answer_matrix


def mnozenie_macierzy(A, B):
    nrow_A = len(A)
    ncol_A = len(A[0])
    nrow_B = len(B)
    ncol_B = len(B[0])
    assert ncol_A == nrow_B
    result = [[0] * ncol_B for i in range(nrow_A)]
    for i in range(nrow_A):
        for j in range(ncol_B):
            for k in range(ncol_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
                        

def main(): 
    print("Mozliwe do wykonania ruchy z pozycji (0, 0) dla n = 3 to: ", end="")
    print(mozliwe_ruchy(3, [0, 0]))

    #test II
    # for i in range(8): 
    #     for j in range(8): 
    #         print(liczba_na_pozycje(8, pozycja_na_liczbe(8, [i, j])), end = " ")
    #     print()
    # works fine

    print(f"Pozycje [0, 0] tlumacze na {pozycja_na_liczbe(10, [0, 0])}")
    print(f"Liczbe 0 tlumacze na {liczba_na_pozycje(10, 0)}")
    for wiersz in macierz_przejscia(2): # Skoczek na szachownicy 2x2 nie ma zadnych ruchow
        print(" ".join(f"{x:.2f}" for x in wiersz)) # Ladniejsze printowanie

    #W funkcji main oblicz, jakie jest prawdopodobieństwo, że startując z pola (0, 0) \
    # skoczek wyląduje na polu (0, n − 1) podokładnie stu ruchach
    # p = v * M * M^(k-1)
    n = 16
    M = macierz_przejscia(16)
    v = [[0 for _ in range(n*n)]] #sztucznie macierz 1 x n^2
    v[0][0] = 1
    p = mnozenie_macierzy(v,M)
    k = 99
    for _ in range(k - 1): 
        p = mnozenie_macierzy(p, M)
    print(p[0][n - 1])
    

if __name__ == '__main__': 
    main()



import csv
import math
import matplotlib.pyplot as plt


def distance(u: list[float, float], v: list[float, float]) -> float: 
    dist: float = 0
    for i in range(len(u)): 
        dist += ((u[i] - v[i]) ** 2)
    return math.sqrt(dist)


def nearest_neighbor_class(A: list[list[float, float]], c: list[int], z: list[float, float]) -> int: 
    minium: float = float("inf")
    where_minimum: int = -1
    for i in range(len(A)): 
        if distance(A[i], z) < minium: 
            minium = distance(A[i], z)
            where_minimum = i
    return c[where_minimum]


def knn(A: list[list[float, float]], c: list[int], Z: list[list[float, float]]) -> list[int]: 
    test_c: list[int] = [0] * len(Z)
    for i in range(len(Z)): 
        test_c[i] = nearest_neighbor_class(A, c, Z[i])
    return test_c


def confusion_matrix(new_c: list[int], true_c: list[int]) -> None: 
    #All of em r integers
    TN, FP, FN, TP = 0, 0, 0, 0
    for i in range(len(new_c)):
        if new_c[i] == 0 and true_c[i] == 0: 
            TN += 1
        elif new_c[i] == 0 and true_c[i] == 1: 
            FN += 1
        elif new_c[i] == 1 and true_c[i] == 0: 
            FP += 1
        else: 
            TP += 1
    accuracy: float = ( TP + TN ) / ( TP + TN + FP + FN)
    precision: float = TP / ( TP + FP)
    recall: float = TP / ( TP + FN )
    F1: float = ( 2 * TP ) / ( 2 * TP + FP + FN )
    with open("output.txt", "w") as f: 
        print("  |  0  |  1  ", file = f)
        print("-------------", file = f)
        print(f"0 | {TN:2d}  | {FP:2d} ", file = f)
        print(f"1 | {FN:2d}  | {TP:2d} ", file = f)
        print(file = f)
        print(f"Dokladnosc = {accuracy:.2f}", file = f)
        print(f"Precyzja = {precision:.2f}", file = f)
        print(f"Czulosc = {recall:.2f}", file = f)
        print(f"Miara F1 = {F1:.2f}", file = f)


def visualize(A: list[list[float, float]], c: list[int]) -> None: 
    #a0, a1, b0, b1, (all floats)
    a0, a1 = math.inf, -math.inf
    b0, b1 = math.inf, -math.inf
    for i in range(len(A)): 
        if A[i][0] < a0: 
            a0 = A[i][0]
        if A[i][0] > a1: 
            a1 = A[i][0]
        if A[i][1] < b0: 
            b0 = A[i][1]
        if A[i][1] > b1:
            b1 = A[i][1]
    N: int = int(input("Podaj N: "))
    r: float = (a1 - a0) / (N - 1)
    t: float = (b1 - b0) / (N - 1)
    x: list[float] = [a0 + i * r if i != N - 1 else a1 for i in range(N)]
    y: list[float] = [b0 + i * t if i != N - 1 else b1 for i in range(N)]
    xy_zipped: list[list[float, float]] = []
    for i in range(N):
        for j in range(N): 
            xy_zipped.append([x[i], y[j]])
    xy_class: list[int] = knn(A, c, xy_zipped)
    #temporary lists just for making visualization aka list[float]
    u, v, u2, v2 = [], [], [], []
    for i in range(len(A)): 
        if c[i] == 0:
            u.append(A[i][0])
            v.append(A[i][1])
        else:
            u2.append(A[i][0])
            v2.append(A[i][1])
    #temporary lists just for making visualization aka list[float]
    x1, y1, x2, y2 = [], [], [], []
    for i in range(len(xy_zipped)):
        if xy_class[i] == 0:
            x1.append(xy_zipped[i][0])
            y1.append(xy_zipped[i][1])
        else:
            x2.append(xy_zipped[i][0])
            y2.append(xy_zipped[i][1])
    # code making real visualization
    fig = plt.figure()
    plt.scatter(u, v, color = "r")
    plt.scatter(u2, v2, color = "b")
    plt.scatter(x1, y1, marker = ".", alpha = 0.2, color = "r")
    plt.scatter(x2, y2, marker = ".", alpha = 0.2, color = "b")
    fig.savefig("output.png", dpi=90)


def read_classes(path: str) -> list[int]: 
    c: list[int] = []
    with open(path, "r") as f: 
        for line in f: 
            line = int(line.strip())
            c.append(line)
    return c


def read_wine_data(path: str) -> list[list[float, float]]: 
    wine_data: list[list[float, float]] = []
    with open(path, "r") as f: 
        for row in csv.reader(f): 
            for i in range(len(row)): 
                row[i] = float(row[i])
            wine_data.append(row)
    return wine_data


def main() -> None: 
    A: list[list[float, float]] = read_wine_data("train_wine.csv")
    c: list[int] = read_classes("train_class.txt")
    Z: list[list[float, float]] = read_wine_data("test_wine.csv")
    new_c: list[int] = knn(A, c, Z)
    true_c: list[int] = read_classes("test_class.txt")
    # print(len(new_c), len(true_c)) # works fine
    confusion_matrix(new_c, true_c) 
    # print(len(c), len(A)) # works fine
    visualize(A, c)
        

if __name__ == "__main__": 
    main()

import numpy as np
from sklearn import datasets, svm
# inicjowanie rysunku:
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def F(a: float, b: float) -> float:
    """
    Nie interesuje nas, co funkcja robi:
    traktujemy ja jako "czarna skrzynke".
    Wazne jest jedynie to, ze F(a, b) zwraca wartość z przedzialu [0,1]
    dla a, b > 0
    Przykład inspirowany http://scikit-learn.org/stable/auto_examples/
    exercises/plot_iris_exercise.html
    """
    iris = datasets.load_iris() # zbior iris
    X, y = iris.data, iris.target
    X, y = X[y != 0, :2], y[y != 0] # tylko klasy 1 i 2
    n_sample = len(X)
    np.random.seed(1234)
    order = np.random.permutation(n_sample)
    X = X[order]
    y = y[order]
    X_train = X[:int(0.8 * n_sample)] # proba uczaca = losowe 80%
    y_train = y[:int(0.8 * n_sample)]
    X_test = X[int(0.8 * n_sample):] # proba testowa = pozostale 20%
    y_test = y[int(0.8 * n_sample):]
    clf = svm.SVC(gamma=a, C=b) # support vector classifier
    clf.fit(X_train, y_train)
    return np.mean(clf.predict(X_test) == y_test) # accuracy, wartość z [0,1]


def main() -> None: 
    #odczyt danych z pliku
    with open("ZadaniaPunktowane/2017-IAD-05/input.txt", "r") as file:
        a1: float = float(file.readline().strip())
        an: float = float(file.readline().strip())
        n: int = int(file.readline().strip())
        b1: float = float(file.readline().strip())
        bm: float = float(file.readline().strip())
        m: int = int(file.readline().strip())
    
    if not(a1 < an and b1 < bm and n > 1 and m > 1):
        raise ValueError("Błędne dane!")
    
    fmin: float = float("inf")
    fmax: float = -float("inf")
    max_a: int
    max_b: int
    max_a, max_b = -1, -1 
    out_file = open("ZadaniaPunktowane/2017-IAD-05/output.txt", "w")
    print("a \ b | ",end="",file = out_file)
    for i in range(n + 2):
        if i == 0:
            for j in range(m):
                print(f"{b1 * (j + 1):.2f}", "", end="",file = out_file)
        elif i == 1:
            print("------|", end="",file = out_file)
            for j in range(m * 5):
                print("-",end="",file = out_file)
        else:
            if a1 * (i - 1) < 100:
                print(a1 * (i - 1), " | ", end="",file = out_file)
            else:
                print(a1 * (i - 1), "| ", end="",file = out_file)
            for j in range(m):
                curr_value = F(a1 * (i - 1), b1 * (j + 1))
                if curr_value > fmax:
                    fmax = curr_value
                    max_a = a1 * (i - 1)
                    max_b = b1 * (j + 1)
                if curr_value < fmin: 
                    fmin = curr_value
                    min_a = a1 * (i - 1)
                    min_b = b1 * (j + 1)
                print(f"{curr_value:.2f}", "", end="",file = out_file)
        print(file = out_file)
    print(f"fmin = {fmin}, fmax = {fmax}, a wartość największa jest osiągana dla a = {max_a}, b = {max_b}",file = out_file)
    out_file.close()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ustal zakresy na osiach:
    ax.set_xlim([a1, a1 * n]) # zakres wartości na osi OX [xmin, xmax]
    ax.set_ylim([b1, b1 * m]) # zakres wartości na osi OY [ymin, ymax]
    # przykładowy jasnoszary prostokąt o wierzchołkach (0.1, 0.5) i (0.6, 2.75):
    for i in range(1, n + 1): 
        for j in range(1, m + 1):
            ax.add_patch(patches.Rectangle(
            (a1 * i, b1 * j), # (x,y)
            a1, # szerokosc
            b1, # wysokosc
            facecolor=str(F(a1 * i, b1 * j)) # stopien szarosci (od 0 do 1) jako napis
            ))
    # ax.add_patch(patches.Rectangle(....)) można będziemy wywoływać wielokrotnie
    # zapis do PNG po zakończeniu rysowania
    fig.savefig('ZadaniaPunktowane/2017-IAD-05/output.png', dpi=90)


if __name__ == "__main__": 
    main()

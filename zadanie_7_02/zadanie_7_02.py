import csv
import matplotlib.pyplot as plt
import math

def get_iris_data() -> list[list[float]]: 
    iris = []
    f = open("iris.csv", "r") # r=do odczytu
    for row in csv.reader(f):
        for i in range(len(row)):
            row[i] = float(row[i]) # konwersja z str na float
        list.append(iris, row) # == A.append(row)
    f.close()
    return iris


def transposition(iris: list[list[float]]): 
    after_transposition = []
    for i in range(4): 
        tmp = []
        for j in range(150): 
            tmp.append(iris[j][i])
        after_transposition.append(tmp)
    return after_transposition


def graph(iris: list[list[float]]) -> None: 
    plt.figure(figsize=[16,16], dpi=72)
    feature_names = ["sepal length", "sepal width", "petal length", "petal width"]
    fig, axs = plt.subplots(4, 4)
    for n in range(4): 
        for m in range(4): 
            axs[n, m].scatter(iris[m], iris[n], color = "b", marker = ".", alpha = 0.2)
            a,b = least_squares_fit(iris[m], iris[n])
            axs[n, m].plot(iris[m], [a * x + b for x in iris[m]], color = "r")
            axs[n, m].set_xlabel(feature_names[m])
            axs[n, m].set_ylabel(feature_names[n])     
    plt.savefig("output.png")


def calculate_average(listt: list[float]) -> float: 
    sum = 0
    for i in range(len(listt)): 
        sum += listt[i]
    return sum / len(listt)


def calcurate_Pearsons_coefficent(x: list[float], y: list[float]) -> float:
    top = 0
    left_bottom, right_bottom = 0, 0
    x_average = calculate_average(x)
    y_average = calculate_average(y)
    for i in range(len(x)): 
        top += ((x[i] - x_average) * (y[i] - y_average))
        left_bottom += ((x[i] - x_average)**2) 
        right_bottom += ((y[i] - y_average)**2)
    return ( top / math.sqrt(left_bottom * right_bottom) )


def create_matrix_of_Pearsons_coefficents(iris: list[list[float]]) -> list[list[float]]: 
    matrix = [] * 4
    for i in range(4): 
        tmp = []
        for j in range(4): 
            tmp.append(calcurate_Pearsons_coefficent(iris[i], iris[j]))
        matrix.append(tmp)
    return matrix


def least_squares_fit(x: list[float], y: list[float]) -> tuple[float, float]: 
    x_average = calculate_average(x)
    y_average = calculate_average(y)
    numerator = sum((x[i] - x_average) * (y[i] - y_average) for i in range(len(x)))
    denominator = sum((x[i] - x_average)**2 for i in range(len(x)))
    a = numerator / denominator
    b = y_average - a * x_average
    return a, b


def main() -> None: 
    iris: list[list[float, float, float, float]] = get_iris_data()
    iris = transposition(iris)
    graph(iris)
    matrix_of_Pearsons_coefficents = create_matrix_of_Pearsons_coefficents(iris)
    print(matrix_of_Pearsons_coefficents)


if __name__ == "__main__": 
    main()
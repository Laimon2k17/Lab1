import random


def generateRandomMatrix(m=None, n=None, min_limit=0, max_limit=100):
   
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = random.randint(min_limit, max_limit)  # случайное значение в заданном диапазоне
            row.append(num)
        matrix.append(row)

    return matrix


m = int(input("Введите количество строк матрицы: "))
n = int(input("Введите количество столбцов матрицы: "))
min_limit = int(input("Введите минимальное значение: "))
max_limit = int(input("Введите максимальное значение: "))

random_matrix = generateRandomMatrix(m, n, min_limit, max_limit)
print("Вывод матрицы:")
for row in random_matrix:
    print(row)

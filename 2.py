import random


def generateRandomMatrix(m=None, n=None, min_limit=0, max_limit=100):
   
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            num = random.randint(min_limit, max_limit)  
            row.append(num)
        matrix.append(row)

    return matrix


m = int(input("Количество строк матрицы: "))
n = int(input("Количество столбцов матрицы: "))
min_limit = int(input("Минимальное значение элементов в матрице: "))
max_limit = int(input("Максимальное значение элементов в матрице: "))

random_matrix = generateRandomMatrix(m, n, min_limit, max_limit)
print("Результат:")
for row in random_matrix:
    print(row)

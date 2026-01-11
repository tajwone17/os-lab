column = 7

n = int(input("Enter the number of rows: "))

matrix = []
for i in range(n):
    row = []
    for j in range(column):
        row.append(0)
    matrix.append(row)


for i in range(n):
    print(f"Enter the value for {i+1}th row: ", end="")
    a, b, c = map(int, input().split())
    matrix[i][0] = a
    matrix[i][1] = b
    matrix[i][2] = c

print("\nFinal Matrix :")
for row in matrix:
    print(*row)
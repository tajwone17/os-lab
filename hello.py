# print("Hello world")
# print("My name is Murad")

column = 7

n = int(input("Enter number of rows: "))

matrix = []
for i in range(n):
    row = []
    for j in range(column):
        row.append(0)
    matrix.append(row)


for i in range(n):
    print(f"{i+1} : ", end="")
    a, b, c = map(int, input().split())
    matrix[i][0] = a
    matrix[i][1] = b
    matrix[i][2] = c

print("\nMatrix :")
for row in matrix:
    print(*row)
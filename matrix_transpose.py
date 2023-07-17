R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
swap = 0
for i in range(R):
    for j in range(C):
        if i<j:
            swap = matrix[i][j]
            matrix[i][j]=matrix[j][i]
            matrix[j][i]=swap
print(matrix)
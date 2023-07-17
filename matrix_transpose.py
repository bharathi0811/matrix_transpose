R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries rowwise:")
for i in range(R):
    a =[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
transpose  = [list(row) for row in zip(*matrix)]
print(transpose)

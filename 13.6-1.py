X=[[1,4,6],[3,4,7],[6,8,3]]
Y=[[3,6,9],[6,10,9],[7,6,4]]
Z=[[0,0,0],[0,0,0],[0,0,0]]

print("X的矩阵:")
for x in X:
    print(x)
print("\nY的矩阵:")
for y in Y:
    print(y)

for i in range(len(X)):
    for j in range(len(X[0])):
        Z[i][j]=X[i][j]+Y[i][j]

print("\nZ的矩阵:")
for z in Z:
    print(z)

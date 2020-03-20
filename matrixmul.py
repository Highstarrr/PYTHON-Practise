#计算两个n*n矩阵的Hadamard乘积
n = int(input("Enter the value of n:"))
print("Enter values of the Matrix A:")
a = []
for i in range(n):
    a.append([int(x) for x in input().split()]) #split() split( )
print("Enter values of the Martrix B:")
b = []
for i in range(n):
    b.append([int(x) for x in input().split()])
c = []
for i in range(n):
    c.append([a[i][j] * b[i][j] for j in range(n)])
print("After matrix multiplication")
print("-"* 7 * n)
for x in c:
    for y in x:
        print(str(y).rjust(5),end='')
    print()
print("-"* 7 * n)

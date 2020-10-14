n = int(input("请输入矩阵的维度："))

t = input("请输入主对角线下方元素：").split(" ")
A3 = [int(t[i])for i in range(len(t))]

t = input("请输入主对角线元素：").split(" ")
A2 = [int(t[i])for i in range(len(t))]

t = input("请输入主对角线上方元素：").split(" ")
A1= [int(t[i])for i in range(len(t))]

t = input("请输入d中的元素：").split(" ")
d = [int(t[i])for i in range(len(t))]

L = []
for i in range(n-1):
    L.append(0)
U = []
for i in range(n):
    U.append(0)
x = []
for i in range(n):
    x.append(0)
y = []
for i in range(n):
    y.append(0)

# 解 L U
U[0] = A2[0]
for i in range(0, n-1):
    L[i] = A3[i] / U[i]
    U[i + 1] = A2[i + 1] - L[i] * A1[i]
print('L矩阵：', L)
print('U矩阵：', U)

# 求 y
y[0] = d[0]
for i in range(n-1):
    y[i+1] = d[i+1]-L[i]*y[i]
print('y矩阵：', y)

x[n-1] = y[n-1]/U[n-1]
for i in range(n-1,0,-1):
    x[i-1] = (y[i-1]-A1[i-1]*x[i])/U[i-1]
print("X={}" .format(x))

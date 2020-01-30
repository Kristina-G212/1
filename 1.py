x = int(input())
n = 100
f = 0  # сумма
t = 0

for i in range(0, n):
    if i == 0:
        t = 1
    else:
        t *= (-1) * (x * x)

    f += t
print(f)
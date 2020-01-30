x = int(input())
n = 100
f = 0  # сумма
t = 0

for i in range(0, n):
    if i == 0:
        t = 1
    else:
        t *= x * x * x / ((2 * i + 1) * (2 * i))

    f += t
print(f)

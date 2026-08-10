n = int(input())

for i in range(10):
    result = n * i
    if result % 2 == 0:
        kind = "even"
    else:
        kind = "odd"

    print(n, "*", i, "=", result," - ", kind)
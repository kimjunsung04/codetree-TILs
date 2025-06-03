a, b = map(int, input().split())

for i in range(1, 10):
    for j in range(b, a-2, -2):
        print(f"{j} * {i} = {j*i}", end="")
        if j > 2: print(" / ", end="")
    print()
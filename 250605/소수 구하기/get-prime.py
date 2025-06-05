n = int(input())

for i in range(2, n+1):
    sosu_ck = True
    for j in range(1, i+1):
        if j != 1 and i != j and i % j == 0:
            sosu_ck = False
            break
    if sosu_ck:
        print(i, end=" ")
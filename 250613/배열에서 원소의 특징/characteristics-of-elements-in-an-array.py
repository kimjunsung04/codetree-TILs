n_list = list(map(int, input().split()))

for i in range(len(n_list)):
    if n_list[i] % 3 == 0:
        print(n_list[i-1])
        break
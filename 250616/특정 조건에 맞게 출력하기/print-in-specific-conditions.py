n_list = list(map(int, input().split()))

for i in n_list[:-1]:
    if i % 2 == 0:
        print(i//2, end=" ")
    else:
        print(i+3, end=" ")
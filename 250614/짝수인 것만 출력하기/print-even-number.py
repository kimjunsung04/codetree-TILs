n = int(input())
n_list = list(map(int, input().split()))

for i in n_list:
    if i % 2 == 0:
        print(i, end=" ")
n = int(input())

n_list = [list(map(int, input().split())) for _ in range(n)]

for a, b in n_list:
    odd_sum = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            odd_sum += i
    print(odd_sum)
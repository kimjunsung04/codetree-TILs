n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

for a, b in n_list:
    sum_val = 1
    for i in range(a, b+1):
        sum_val *= i
    print(sum_val)
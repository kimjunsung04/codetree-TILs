n = int(input())
n_list = list(map(int, input().split()))
even_list = reversed([i for i in n_list if i % 2 == 0])
print(*even_list)
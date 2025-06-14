n = int(input())
n_list = list(map(int, input().split()))

new_list = [i ** 2 for i in n_list]
print(*new_list)
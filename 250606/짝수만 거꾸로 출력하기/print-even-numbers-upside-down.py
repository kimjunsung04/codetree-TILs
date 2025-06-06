n = int(input())
n_list = list(map(int, input().split()))
odd_list = []

for i in n_list:
    if i % 2 == 0:
        odd_list.append(i)

print(*odd_list[::-1])
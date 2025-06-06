n_list = list(map(int, input().split()))
last = 0
for i in range(len(n_list)):
    if n_list[i] == 0:
        break
    last = i
print(*n_list[last::-1])

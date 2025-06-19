a, b = map(int, input().split())
n_list = [a, b]

for i in range(2, 10):
    n_list.append(n_list[i-1] + n_list[i-2]*2)

for i in n_list:
    print(i, end=" ")
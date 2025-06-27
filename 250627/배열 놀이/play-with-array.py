n, q = map(int, input().split())
n_list = list(map(int, input().split()))

q_list = [list(map(int, input().split())) for _ in range(q)]

for item in q_list:
    num = item[0]
    if num == 1:
        print(n_list[item[1]-1])
    elif num == 2:
        if item[1] not in n_list:
            print(0)
            continue
        print(n_list.index(item[1])+1)
    elif num == 3:
        for i in range(item[1]-1, item[2]):
            print(n_list[i], end=" ")
        print()
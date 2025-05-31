a_list = list(map(int, input().split()))

for i in range(1, 7):
    print(f"{i} - {a_list.count(i)}")
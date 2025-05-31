a_list = list(map(int, input().split()))
count_list = [0 for _ in range(6)]

for item in a_list:
    count_list[item-1] += 1

for i in range(1, 7):
    print(f"{i} - {count_list[i-1]}")
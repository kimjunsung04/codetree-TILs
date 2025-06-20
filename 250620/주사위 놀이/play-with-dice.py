n_list = list(map(int, input().split()))

count_list = [0]*6

for i in n_list:
    count_list[i-1] += 1

for i in range(len(count_list)):
    print(f"{i+1} - {count_list[i]}")
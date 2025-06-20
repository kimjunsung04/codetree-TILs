n = int(input())

n_list = list(map(int, input().split()))

count_list = [0] * 9

for i in n_list:
    count_list[i-1] += 1

for i in count_list:
    print(i) 
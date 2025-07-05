n_list = list(map(int, input().split()))


max_now = n_list[0]
min_now =  n_list[0]
for item in n_list:
    if item in [999, -999]:
        break
    if item > max_now:
        max_now = item
    elif item < min_now:
        min_now = item

print(max_now, min_now)
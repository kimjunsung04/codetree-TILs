n_list = list(map(int, input().split()))

now = n_list[0]

for item in n_list:
    if item > now:
        now = item

print(now)
_ = int(input())
n_list = list(map(int, input().split()))
p_list = []
for item in n_list:
    if item % 5 != 0 and item % 7 != 0:
        p_list.append(item)
print(sum(p_list))
print(f"{sum(p_list)/len(p_list):.1f}")
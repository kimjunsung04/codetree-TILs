a, b = map(int, input().split())
now_list = [a, b]
for i in range(2, 10):
    temp = now_list[i-2] + now_list[i-1]
    if temp >= 10: temp -= 10
    now_list.append(temp)
print(*now_list)
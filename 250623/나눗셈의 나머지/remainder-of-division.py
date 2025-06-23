a, b = map(int, input().split())
count_list = [0]*10
sum_val = 0

while True:
    count_list[a%b] += 1
    a //= b
    if a <= 1: break

for i in count_list:
    sum_val += i ** 2
print(sum_val)
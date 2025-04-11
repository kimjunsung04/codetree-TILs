n = int(input())
s_val = 0
i = 0
while True:
    i += 1
    if i > n:
        break
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    s_val += 1
print(s_val)
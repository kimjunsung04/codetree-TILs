n = int(input())
s_val = 0
for i in range(2, n):
    if i % 2 == 0 and i % 3 == 0 or i % 5 == 0:
        s_val += 1
print(s_val)
n = int(input())
s_val = 0
for i in range(1, 101):
    if s_val+1 > n:
        break
    s_val += 1
print(s_val)
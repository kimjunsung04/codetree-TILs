n = int(input())
s_val = 0
for i in range(1, 101):
    if s_val+i > n:
        break
    s_val += i
print(s_val)
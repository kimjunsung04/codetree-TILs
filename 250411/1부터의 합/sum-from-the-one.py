n = int(input())
s_val = 0
for i in range(1, 101):
    if s_val >= n:
        print(i-1)
        break
    s_val += i
print(100)
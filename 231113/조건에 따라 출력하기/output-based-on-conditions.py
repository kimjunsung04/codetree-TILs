n = int(input())
for _ in range(n):
    n_val = int(input())
    if n_val == 0: break 
    print(int(n_val/3) if n_val % 3 == 0 else n_val+2)
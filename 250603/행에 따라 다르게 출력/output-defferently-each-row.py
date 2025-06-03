n = int(input())

for i in range(1, n+1):
    for j in range(n):
        now_line_val = (n+2)*(i-1) 
        if i == 1: print(j+1, end=" ")
        elif i % 2 == 0:
            print(now_line_val + (2*j), end=" ")
        else:
            if n % 2 != 0:
                print(now_line_val + j, end=" ")
            else:
                print(now_line_val + j+1, end=" ")
    print()
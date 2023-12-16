n = int(input())
if n < 2:
    print('N')
else:
    for i in range(2, n):
        if n % i == 0:
            print('C')
            break
    else:
        print('N')
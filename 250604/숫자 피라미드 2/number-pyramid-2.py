n = int(input())

cnt = 1
for i in range(n):
    for j in range(i+1):
        print(cnt, end=" ")
        cnt+=1
    print()
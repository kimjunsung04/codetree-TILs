n = int(input())

n_list = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for item in n_list:
    if sum(item)/4 >= 60:
        print("pass")
        cnt+=1
    else:
        print("fail")
print(cnt)
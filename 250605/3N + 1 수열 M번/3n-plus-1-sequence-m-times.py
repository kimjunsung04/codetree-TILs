m = int(input())
m_list = [int(input()) for _ in range(m)]

for i in m_list:
    cnt = 0
    while True:
        if i <= 1: break
        if i % 2 == 0:
            i //= 2
        else:
            i *= 3
            i += 1
        cnt += 1
    print(cnt)
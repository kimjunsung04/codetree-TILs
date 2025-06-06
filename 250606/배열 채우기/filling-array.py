n_list = [0 for _ in range(10)]

m_list = list(map(int, input().split()))
last = 0
for i in range(len(m_list)):
    if m_list[i] == 0:
        break
    last = i
    n_list[i] = m_list[i]
print(*n_list[last::-1])

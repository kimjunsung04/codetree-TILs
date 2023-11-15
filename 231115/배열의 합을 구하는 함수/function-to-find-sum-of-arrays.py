n = int(input())
b_list = [[] for _ in range(n+1)]
for i in range(n):
    a_list = list(map(int, input().split()))
    for j in range(len(a_list)):
        b_list[j].append(a_list[j])
    b_list[-1].append(sum(a_list))
    print(f"{' '.join(map(str, a_list))} {sum(a_list)}")
for b_line in b_list:
    print(f"{sum(b_line)}", end=" ")
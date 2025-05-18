n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
t_word_list = [item for item in str if item.startswith(t)]

print(sorted(t_word_list)[k-1])
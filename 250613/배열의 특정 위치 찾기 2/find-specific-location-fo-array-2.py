n_list = list(map(int, input().split()))

odd_sum = sum(n_list[::2])
even_sum = sum(n_list[1::2])

print(max(odd_sum, even_sum) - min(odd_sum, even_sum))
n_list = list(map(int, input().split()))

even_list = n_list[1::2]
odd_list = n_list[2::3]

print(f"{sum(even_list)} {sum(odd_list)/len(odd_list):.01f}")
a_en, a_ma = map(int, input().split())
b_en, b_ma = map(int, input().split())

print(1 if a_en > b_en and a_ma > b_ma else 0)
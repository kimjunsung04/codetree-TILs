n = int(input())

val_val = 0
for num in range(1, n + 1):
    if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        val_val += 1
print(val_val)
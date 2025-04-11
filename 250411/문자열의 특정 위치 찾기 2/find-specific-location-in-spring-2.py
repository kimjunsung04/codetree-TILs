s_list = ["apple", "banana", "grape", "blueberry", "orange"]
s = input()

num = 0
for item in s_list:
    if s in [item[2], item[3]]:
        print(item)
        num += 1
print(num)
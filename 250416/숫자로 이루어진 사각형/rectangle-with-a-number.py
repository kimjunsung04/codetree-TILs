n = int(input())

# Please write your code here.
def print_num_box(n):
    temp_num = 1
    for _ in range(n):
        for _ in range(n):
            print(temp_num, end=" ")
            if temp_num>=9: temp_num = 1
            else: temp_num+=1
        print()

print_num_box(n)
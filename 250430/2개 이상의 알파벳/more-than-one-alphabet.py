A = input()

# Please write your code here.
def check_string_word(a):
    temp_list = []
    for item in list(a):
        if item not in temp_list:
            temp_list.append(item)
        if len(temp_list) >= 2:
            return True
    else:
        return False

print("Yes" if check_string_word(A) else "No")
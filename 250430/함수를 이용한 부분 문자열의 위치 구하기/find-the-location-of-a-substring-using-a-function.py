text = input()
pattern = input()

# Please write your code here.
def str_index_find():
    if not pattern in text:
        return -1
    return text.index(pattern)

print(str_index_find())
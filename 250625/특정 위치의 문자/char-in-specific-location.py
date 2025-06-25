s = input()
s_list =["L", "E", "B", "R", "O", "S"]

if s not in s_list:
    print(None)
else:
    print(s_list.index(s))
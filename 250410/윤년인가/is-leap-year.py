y = int(input())
if y % 100 == 0 and y % 400 != 0:
    print("false")
elif y % 4 == 0:
    print("true")
else:
    print("false") 
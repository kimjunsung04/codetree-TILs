n = int(input())

for i in range(n, 101):
    if i >= 90:
        print("A", end=" ")
    elif i >= 80:
        print("B", end=" ")
    elif i >= 70:
        print("C", end=" ")
    elif i >= 60:
        print("D", end=" ")
    else:
        print("F", end=" ")
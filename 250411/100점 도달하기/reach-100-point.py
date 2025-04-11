n = int(input())
for _ in range(101-n):
    n+=1
    if n > 90:
        print("A", end=" ")
    elif n > 80:
        print("B", end=" ")
    elif n > 70:
        print("C", end=" ")
    elif n > 60:
        print("D", end=" ")
    else:
        print("F", end=" ")
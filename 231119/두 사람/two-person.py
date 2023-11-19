age1, s1 = map(str, input().split())
age2, s2 = map(str, input().split())
if (int(age1) >= 19  and s1 == "M") or (int(age2) >= 19 and s1 == "M"):
    print(1)
else:
    print(0)
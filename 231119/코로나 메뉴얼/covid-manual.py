g1, o1 = map(str, input().split())
g2, o2 = map(str, input().split())
g3, o3 = map(str, input().split())
a_num = 0
if g1 == "Y" and int(o1) >= 37:
    a_num += 1
if g2 == "Y" and int(o2) >= 37:
    a_num += 1
if g3 == "Y" and int(o3) >= 37:
    a_num += 1

print("E" if a_num >= 2 else "N")
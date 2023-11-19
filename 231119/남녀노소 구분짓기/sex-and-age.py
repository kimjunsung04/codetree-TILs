s = int(input())
age = int(input())
if s == 0 and age >= 19:
    print("MAN")
elif s == 0 and age < 19:
    print("BOY")
elif s == 1 and age >= 19:
    print("WOMAN")
elif s == 1 and age < 19:
    print("GIRL")
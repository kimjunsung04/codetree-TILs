cm, kg = map(int, input().split())
bmi = int(kg/((cm/100)*(cm/100)))
print(bmi)
if bmi > 25:
    print("Obesity")
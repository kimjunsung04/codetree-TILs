while True:
    x, y, p = input().split()
    width = int(x)
    height = int(y)
    area = width * height
    print(area)
    if p == 'C':
        break
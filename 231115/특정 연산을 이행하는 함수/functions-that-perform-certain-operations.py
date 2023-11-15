def m_math(n_list):
    for item in n_list:
        if item % 2 == 0:
            print(f"{item//2}", end=" ")
        else:
            print(f"{item*3-20}", end=" ")

a_list = list(map(int, input().split()))
m_math(a_list)
def F(n):
    print(n,end='')
    if n >= 3:
        F(n - 1)
        F(n - 2)
        F(n - 2)
F(4)
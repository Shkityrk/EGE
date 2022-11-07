def f(n):
    if n<=0: return n
    if n>0:
        d = n % 10 + f(n // 10)
        return d
for n in range(1,100000):
    if f(n)>32:
        print(n, f(n))
        break


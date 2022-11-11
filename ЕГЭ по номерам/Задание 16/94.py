def f(n):
    if n<2: return 1
    if n>=2 and n%3==0: return f(n//3)-1
    else: return f(n-1)+17
for i in range(1,1000000):
    if f(i)==110:
        print(i)
        break
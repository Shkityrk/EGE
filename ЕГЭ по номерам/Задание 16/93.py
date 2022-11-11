def f(n):
    if n<2: return 1
    if n>=2 and n%3==0: return f(n/3)-1
    if n>=2 and n%3!=0: return f(n-1)+7
for n in range(1,1000000):
    r=f(n)
    if r==111:
        print(n)
        break


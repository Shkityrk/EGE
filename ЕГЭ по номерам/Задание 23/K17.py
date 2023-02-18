def f(c,e):
    if c>e: return 0
    if c==e: return 1
    if c<e: return f(c+2,e)+f(c+4,e)+f(c+5,e)
for i in range(32,100000):
    if f(31,i)==1001:
        print(i)


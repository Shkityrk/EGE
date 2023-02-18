def f(c,e):
    b=bin(c)[2:]
    b1=str(b)
    b1=b1.replace('1','0')
    b1='1'+b1[:-1]

    if c<e: return 0
    if c==e: return 1
    if c>e: return f(c-1,e)+f(int(b1,2),e)
print(f(17,1))

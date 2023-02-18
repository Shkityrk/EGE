def f(c,e):
    b=str(bin(c)[2:])
    b1=b+'0'
    b2=b+'1'
    if c>e: return 0
    if c==e: return 1
    else: return f(c+1,e)+f(int(b1,2),e)+f(int(b2,2),e)
print(f(4,29))

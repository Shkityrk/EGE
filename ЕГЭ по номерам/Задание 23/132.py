def f(c,e):
    b=bin(c)[2:]
    b1=str(b)+'0'
    b2=str(b)+'1'

    if c>e: return 0
    if c==e: return 1
    else: return f(c+1,e)+f(int(b1,2),e)+f(int(b2,2),e)

print(f(5,46))
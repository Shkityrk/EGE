ch=set()
def f(c,s):
    if s==8:
        if 1000<=c<1024: ch.add(c)
    else: return f(c+1,s+1),f(c+5,s+1),f(c*3,s+1)
f(1,0)
print(len(ch))

d=set()
def f(c,s):
    if s==15:
        d.add(c)
    else:
        f(c*2,s)
        f(c*2+1,s)
f(1,0)
print(len(d))
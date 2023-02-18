
def f(c,e):
    if c>e or c==33: return 0
    if c==e:return 1
    else: return f(c+2,e)+f(int(g(c)),e)
a=[]
for x in range(2,48):
    if 2**(x-1)%x==1: a.append(x)
def g(c):
    for i in range(len(a)):
        if a[i]>c: return a[i]

print(f(2,14)*f(14,45))

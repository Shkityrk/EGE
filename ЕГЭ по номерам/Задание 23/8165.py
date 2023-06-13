def f(c,e):
    if c>e:return 0
    if c==e:return 1
    return f(c+1,e)+f(c*2,e)+f(c*3,e)
k=0
for n in range(2,15,2):
    k+=f(n,15)
print(k)
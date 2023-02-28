def f(c,e,p):
    if c>e:return 0
    if c==e:return p<=2
    if c<e:return f(c+1,e,p)+f(c*2,e,p+1)+f(c*3,e,p+1)

print(f(1,100,0))
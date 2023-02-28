def f(c,e,k1,k2):
    if c>e:return 0
    if c==e :return k1>k2
    if c<e:return f(c+1,e,k1,k2+1)+f(c*2,e,k1+1,k2)+f(c*3,e,k1+1,k2)
print(f(1,157,0,0))
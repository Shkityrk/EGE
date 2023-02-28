def f (c,e,k1,k2,k3):
    if c>e: return 0
    if c==e: return k1<=4 and k2>=2 and k3==5
    if c<e:return f(c*5,e,k1+1,k2,k3)+f(c*3,e,k1,k2+1,k3)+f(c+45,e,k1,k2,k3+1)
print(f(1,2970,0,0,0))
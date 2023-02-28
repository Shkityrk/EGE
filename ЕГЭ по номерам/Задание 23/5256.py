def f(c,e,k):
    if c%2!=0:k+=1
    if c>e:return 0
    if c==e:return k<=7
    if c<e:return f(c+2,e,k)+f(c*2,e, k)+f(c*3,e,k)
print(f(1,214,0))
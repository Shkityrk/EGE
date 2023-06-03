def f(c,e,s):
    if c%2==0:s+=1
    if c>e or s>8:return 0
    if c==e:return s==6
    else:return f(c+1,e,s)+f(c+3,e,s)+f(c+5,e,s)
print(f(3,25,0))
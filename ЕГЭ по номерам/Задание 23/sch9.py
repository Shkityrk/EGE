def f(c,e):
    if c>e:return 0
    if c==e:return 1
    else:return f(c+1,e)+f(c+4,e)+f(c*2,e)
print(f(10,18)*f(18,36))
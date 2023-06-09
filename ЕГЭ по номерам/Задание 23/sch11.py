def f(c,e):
    if c>e or c==10 or c==20:return 0
    if c==e:return 1
    else:return f(c+1,e)+f(c+2,e)+f(c*3,e)
print(f(3,15)*f(15,30))
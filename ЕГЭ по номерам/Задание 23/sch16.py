def f(c,e):
    if c>e or c==8 or c==15:return 0
    if c==e:return 1
    else:return f(c+1,e)+f(c+2,e)+f(c*3,e)
print(f(3,10)*f(10,22))
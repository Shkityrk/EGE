def f(c,e):
    if c>e or c==40:return 0
    if c==e:return 1
    else:return f(c+1,e)+f(c*3,e)
print(f(1,16)*f(16,60))
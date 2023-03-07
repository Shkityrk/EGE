def f(c,e):
    if c<e or c==4:return 0
    if c==e:return 1
    else:return f(c-1,e)+f(c//2,e)
print(f(60,20)*f(20,1))
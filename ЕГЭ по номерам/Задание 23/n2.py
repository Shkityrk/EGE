def f(c,e):
    if c<e or c==50:return 0
    if c==e:return 1

    if c%2==0:return f(c-5,e)+f(c-4,e)+f(c//2,e)
    else:return f(c-5,e)+f(c-4,e)
print(f(100,73)*f(73,22)*f(22,2))
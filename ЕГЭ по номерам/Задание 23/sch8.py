def f(c,e):
    if c<e:return 0
    if c==e:return 1
    else:return f(c-5,e)+f(c-7,e)
print(f(101,37)*f(37,20))
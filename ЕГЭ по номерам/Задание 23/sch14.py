def f(c,e):
    if c>e :return 0
    if c==e:return 1
    else:return f(c+1,e)+f(c+2,e)+f(c*2,e)
print(f(3,9)*f(9,11)*f(11,13))
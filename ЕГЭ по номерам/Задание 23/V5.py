def f(c,e):
    if c>e:return 0
    if c==e:return 1
    else:return f(c+2,e)+f(c+7,e)
print(f(5,49))
def f(c,e):
    if c>e or c==21:return 0
    if c==e:return 1

    return f(c+1,e)+f(2*c+1,e)

print(f(1,25))
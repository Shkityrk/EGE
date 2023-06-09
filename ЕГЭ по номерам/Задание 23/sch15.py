a=[x**2 for x in range(2,8)]
def f(c,e):
    if c<e:return 0
    if c==e:return 1
    if c in a: return f(c-2,e)+f(c-3,e)+ f(c**0.5,e)
    else:return f(c-2,e)+f(c-3,e)
print(f(25,3))
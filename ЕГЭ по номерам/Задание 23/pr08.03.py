def f(c,e,su, pr):
    if c>e:return 0
    if c==e:return pr>su
    if c<e:return f(c+1,e,su+1,pr)+f(c*2,e,su,pr+1)+f(c*5,e,su,pr+1)
print(f(3,260,0,0))
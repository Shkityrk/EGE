def f(n):
    if n>=10000: return n
    elif n%4==0: return n*4+f(n*4-2)
    else: return -1+f(n-2)

for n in range(1,200):
    try: print(n, f(n))
    except: pass

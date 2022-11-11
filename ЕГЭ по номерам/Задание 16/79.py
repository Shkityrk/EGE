def f(n):
    if n<=5: return n
    if n>5 and n%3==0: return n+f(n/3+1)
    if n > 5 and n % 3!= 0: return n+f(n+3)
for i in range(1,10000):
    try:
        if f(i)>1000:
            print(i)
            break
    except: pass
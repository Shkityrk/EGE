def f(n):
    if n<3: return n+1
    if n%2==0: return f(n-2)+n-2
    if n%2!=0: return f(n+2)+n+2
k=0
for n in range(1,80000):
    try:
        if 10000<=f(n)<100000:
            k+=1
    except:...
print(k)
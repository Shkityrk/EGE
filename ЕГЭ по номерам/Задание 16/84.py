def f(n):
    if n<2: return n
    if n>=2 and n%2==0: return f(n/2)+1
    if n>=2 and n%2!=0: return f(3*n+1)+1
k=0
for n in range(1,101):
    try:
        if f(n)>100:k+=1
    except: pass
print(k)
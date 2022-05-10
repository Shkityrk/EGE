def f(n):
    if n==1 or n==2: return 1
    else: return f(n-1)+f(n-2)
k=0
for i in range(1,22):

    k+=(f(i)**2-f(i))
    print(i,f(i)**2-f(i), k )
print(k)
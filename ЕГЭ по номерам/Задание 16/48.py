def f(n):
    if n<=3: return n
    if n>3 and n%2==0: return n+f(n-1)
    if n>3 and n%2!=0: return n*n+f(n-2)
k=0
for n in range(1,2000):
    if f(n)<10**8:k+=1
print(k)
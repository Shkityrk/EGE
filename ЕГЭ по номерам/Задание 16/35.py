'''def f(n,m):
    if n < m: n,m = m,n
    if n != m: return f(n - m, m)
    else: return n
for n in range(1,10000):
    for m in range(1,10000):
        if n!=m:
            if f(n,m)>15:
                print(n+m)
                break'''
def F(n,m):
 if n<m:
  n,m = m,n
 if n != m:
   return F(n-m,m)
 else:
   return n

for n in range(1,500):
    for m in range(1,500):
        if n!=m:
            if F(n,m)>15:
                print(n, m , F(n,m))



k=0
def f(n):
    global k
    k+=n*n
    if n>1:
        k+=2*n+1
        f(n-2)
        f(n//3)
f(100)
print(k)
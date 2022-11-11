cache={}
def f(n):
    if n not in cache:
        if n<-100: cache[n]= 1
        elif n>10: cache[n]= f(n-1)+3*f(n-3)+2
        else: cache[n]= -f(n-1)
    return cache[n]
print(f(20))
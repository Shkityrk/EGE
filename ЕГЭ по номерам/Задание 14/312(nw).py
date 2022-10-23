o=0
for x in range(2,10000):
    k=0
    n=7**500+7**200-7**50-x
    while n!=0:
        k+=n%7
        n//=7
    o=max(k,o)
print(o)

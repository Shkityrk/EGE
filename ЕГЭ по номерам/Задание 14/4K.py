n=51*7**12-7**3-22
k=0
while n!=0:
    k+=n%7
    n//=7
print(k)
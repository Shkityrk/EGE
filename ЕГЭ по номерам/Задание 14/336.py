n=abs(3*5**1984-7*25**777-11*125**666-404)
##ABS, блин...

k=0
while n!=0:
    if n%5==2:k=k+1
    n=n//5
print(k)
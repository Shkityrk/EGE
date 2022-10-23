n=8**1014-2**530-12
k=0
while n!=0:
    if n%2==1: k+=1
    n=n//2
print(k)
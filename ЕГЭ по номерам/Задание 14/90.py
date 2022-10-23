n=4**2016+2**2018-6
k=0
while n!=0:
    if n%2==1: k+=1
    n=n//2
print(k)
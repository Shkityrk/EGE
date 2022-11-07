n=64**30+2**300-4
k=0
while n!=0:
    if n%8==7:k+=1
    n//=8
print(k)
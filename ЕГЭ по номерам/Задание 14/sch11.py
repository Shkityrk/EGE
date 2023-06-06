k=0
n=2*64**123-8**98+111
while n!=0:
    if n%8==0:k+=1
    n=n//8
print(k)
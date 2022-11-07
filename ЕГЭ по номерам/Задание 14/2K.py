n=3*16**8-4**5+3
k=0
while n!=0:
    if n%4==3:k+=1
    n//=4
print(k)
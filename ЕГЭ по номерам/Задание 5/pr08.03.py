k=0
for n in range(1,10000):
    b=bin(n)[2:]
    s=str(b)

    if n%2==0:s=s+str(bin(s.count('1'))[2:])
    else: s='1'+s+'00'

    r=int(s,2)
    if 500<=r<=700:k+=1
print(k)
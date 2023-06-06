mn=10**10
for n in range(172,1000):
    b=bin(n)[2:]
    s=str(b)
    if s.count('1')%2==0:s=s+'00'
    else:s=s+'11'
    r=int(s,2)

    if r%2==0:mn=min(mn,r)
print(mn)



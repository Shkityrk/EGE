mx=0
for n in range(1,1000):
    s=str(bin(n)[2:])
    if n%2==0:s=s+'11'
    else: s=s+'10'
    r=int(s,2)
    if r<128:
        mx=max(mx,r)
print(mx)
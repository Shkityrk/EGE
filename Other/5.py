mx=0
for n in range(1,1000):
    b=bin(n)[2:]
    s=str(b)
    if n%2!=0:s='1'+s+'0'
    else:s='11'+s+'11'

    r=int(s,2)
    if r<126:mx=max(r,mx)
print(mx)


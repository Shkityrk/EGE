ans=10**10
for n in range(1,1000):
    s=str(bin(n)[2:])
    s=s+s[-1]
    if s.count('1')%2==0:s=s+'0'
    else:s=s+'1'
    if s.count('1') % 2 == 0:
        s = s + '0'
    else:
        s = s + '1'

    r=int(s,2)
    if r>204:
        ans=min(r,ans)

print(ans)

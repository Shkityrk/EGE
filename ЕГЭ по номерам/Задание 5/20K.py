n=120
for m in range(1,1000):
    s=str(m)
    p=2
    pn=1
    a=[]
    for i in range(len(s)):
        if int(s[i])%2==0 and s[i]!='0':p=p*int(s[i])
        if int(s[i])%2!=0: pn=pn*int(s[i])

    r=abs(p-pn)
    if r==29:
        print(m)
        break

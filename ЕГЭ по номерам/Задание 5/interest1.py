k=0
for n in range(1000,10000):
    s=str(n)
    if int(s[0])%4==0: s='9'+s[1:]
    

    r=int(s)
    if s[0]=='9' and r%8==4:k+=1
print(k)

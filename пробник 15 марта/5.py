k=0
for n in range(1000,10000):
    s=str(n)
    if int(s[0])%4==0:s='9'+s[1:]
    if int(s[0])%2==0 and int(s[0])%4!=0:s='3'+s[1:]

    if s[0]=='9':
        if int(s)%8==4:
            k+=1
            print(s)
print(k)
for n in range(1,256):
    b=bin(n)[2:]
    s=str(b)
    while len(s)<8:
        s='0'+s
    l=''
    for i in range(len(s)):
        if s[i]=='1':l+='0'
        else: l+='1'    
    r=int(l,2)+1    
    if r==221:
        print(n)

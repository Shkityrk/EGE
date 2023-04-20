for n in range(1,100000000):
    s=str(n)
    s1=0
    s2=0
    #1234567
    #012345
    for i in range(len(s)):
        if int(s[i])%2!=0:s1+=int(s[i])
        if i%2!=0:s2+=int(s[i])
    r=abs(s1-s2)
    if r==29:
        print(n)
        break
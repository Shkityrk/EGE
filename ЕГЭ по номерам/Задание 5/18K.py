for n in range(1,10000):
    s=str(n)
    s_chet=0
    s_i=0
    for i in range(len(s)):
        if int(s[i])%2==0:
            s_chet+=int(s[i])
        if i%2!=0:
            s_i+=int(s[i])
    r=abs(s_chet-s_i)
    if r==9:
        print(n)
        break

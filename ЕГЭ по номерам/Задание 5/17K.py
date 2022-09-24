for n in range(10,1000):
    s=str(n)
    a=[]
    for i in range(len(s)-1):
        a+=[int(s[i]+s[i+1])]
    r=max(a)-min(a)
    if r==44:
        print(n)
        
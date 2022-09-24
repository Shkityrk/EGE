for n in range(300,401):
    s=str(n)
    a=[s[0]+s[1], s[0]+s[2], s[1]+s[0],s[1]+s[2],s[2]+s[0],s[2]+s[1]]
    a=[int(c) for c in a if c[0]!='0']
    r=max(a)-min(a)
    if r==20:
        print(n)
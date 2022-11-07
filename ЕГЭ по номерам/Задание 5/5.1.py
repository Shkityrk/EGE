for n in range(1,1000):
    b=bin(n)[2:]
    s=str(b)
    if n%2==0:s+='0'
    else: s+='1'

    if s.count('1')%3==0:s='11'+s[2:]
    else:s='10'+s[2:]

    r=int(s,2)
    if r>=26:
        print(n)

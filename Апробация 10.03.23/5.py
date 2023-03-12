for n in range(1,9):
    b=bin(n)[2:]
    s=str(b)
    if n%2==0:s='10'+s
    if n%2!=0:s='1'+s+'01'
    r=int(s,2)
    print(n,r)
#5 101
#7 111
o=0
for n in range(10000,10000000):
    b=bin(n)[2:]
    s=str(b)
    if n%5==0: s=s+'101'
    else: s=s+'1'

    r=int(s,2)
    if r%7==0:s=s+'111'
    else:s=s+'1'

    r=int(s,2)
    if r<1728404:
        print(n,r)
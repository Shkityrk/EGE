for n in range(2,1000):
    s=str(bin(n)[2:])
    s=s[1:]
    s=s.replace('1','*')
    s=s.replace('0','1').replace('*','0')
    s='1'+s
    r=int(s,2)+n
    if r>85 and n%2!=0:
        print(n)
        break

for n in range(1,1000):
    b=bin(int('2'+str(n)))[2:]
    s=str(b)
    if s.count('1')%2!=0:s=s+'1'
    else:s=s+'0'
    if s.count('1')%2!=0:s=s+'1'
    else:s=s+'0'

    r=int(s,2)
    if r>249:
        print(n)
        break
for n in range(94,1000):
    s=str(bin(n)[2:])
    for _ in range(3):
        if s.count('1')==s.count('0'):s=s+s[-1]
        else:
            if s.count('1')>s.count('0'):s=s+'0'
            else:s=s+'1'
    r=int(s,2)
    if r%6==0:
        print(n)
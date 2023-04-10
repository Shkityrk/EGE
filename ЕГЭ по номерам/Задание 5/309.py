for n in range(10,10000):
    s=str(n)
    b=''
    for i in s:
        bi=str(bin(int(i))[2:])
        if bi.count('1')%2==0:bi=bi+'0'
        else: bi=bi+'1'

        if len(bi)==4+1:b+=bi
        elif len(bi)==3+1:b+='0'+bi
        elif len(bi) == 2+1:b += '00' + bi
        elif len(bi) == 1+1:b += '000' + bi
    b='1'+b[2:]+'0'
    r=int(b,2)

    if r==674890:
        print(n)
        break
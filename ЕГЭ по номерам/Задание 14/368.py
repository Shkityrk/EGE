for x in range(0, 10):
    s1='12'+str(x)+'34'
    s2='1'+str(x)+'234'

    if  (int(s1)+9+ int(s2)*2+1)%11==0:print((int(s1)+9+ int(s2)*2+1)//11)

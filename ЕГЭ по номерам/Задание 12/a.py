for k1 in range (1,100):
    s = '1' * k1 + '1' * 100
    while '111' in s:
        s=s.replace('111', '2')
        s=s.replace('222', '1')
        if s.count('1')==1:
            print (k1)

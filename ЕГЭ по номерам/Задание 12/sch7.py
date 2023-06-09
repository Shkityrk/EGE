for i in range(1,100):
    for j in range(1,100):
        s='3'+'1'*i+'4'*j+'3'
        while '31' in s or '34' in s :
            s=s.replace('31','443',1)
            s = s.replace('34', '13', 1)
        if s.count('1')==35 and s.count('4')==44:
            print(i+j)

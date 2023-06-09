for m in range(1,1000):
    for n in range(1, 1000):
        s='1'+'4'*n+'3'*m+'8'
        while '83' in s or '84' in s:
            if '83' in s:s=s.replace('83','33',1)
            if '13' in s:s=s.replace('84', '438',1)

        if s.count('3')==27 and s.count('4')==37:
            print(n)
            break

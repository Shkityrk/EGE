for n1 in range(1,50):
    for n2 in range(1, 50):
        for n3 in range(1, 50):
            s='0'+'1'*n1+'2'*n2+'3'*n3+'0'

            while '00' not in s:
                s=s.replace('01','21022',1)
                s = s.replace('02', '310', 1)
                s = s.replace('03', '230112', 1)

            if s.count('1')==104 and s.count('2')==39 and s.count('3')==83:
                print(n1+n2+n3+2)
                break
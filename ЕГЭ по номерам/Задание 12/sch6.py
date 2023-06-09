for i in range(1,50):
    for j in range(1,50):
        for k in range(1, 50):
            s='1'+'2'*i+'3'*j+'4'*k+'1'
            while not('11' in s):
                s=s.replace('12','41',1)
                s = s.replace('12', '41', 1)
                s = s.replace('13', '21', 1)
                s = s.replace('14', '31', 1)
            if s.count('2')==17 and s.count('3')==31 and s.count('4')==43:
                print(2+i+j+k)
                break
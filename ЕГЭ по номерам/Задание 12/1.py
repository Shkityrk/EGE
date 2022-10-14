m=100000
for two in range(0,50):
    for two_1 in range(0,50):
        for five in range(0,13):
            for five_1 in range(0, 13):
                s='2'*two+'5'*five+'2'*two_1+'5'*five_1
                k=s.count('2')
                if (s.count('5')==12) and (k>=1):
                    while '25' in s:
                        s=s.replace('25','9',1)
                        if sum(int(c) for c in s)==122:
                            if k<m:
                                m=k
print(m)

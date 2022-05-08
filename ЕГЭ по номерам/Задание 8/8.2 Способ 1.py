s='АНДРЕЙ'
count=0
for s1 in s:
        for s2 in s:
            for s3 in s:
                for s4 in s:
                    for s5 in s:
                        for s6 in s:
                            for s7 in s:
                                n=s1+s2+s3+s4+s5
                                if n.count('А')==1  and n.count('Й')==1:
                                    if s1 !='Й':
                                        count+=1
print (count)
s='12345'
k=0
for i1 in s:
    if i1 != '0':
        for i2 in s:
            for i3 in s:
                for i4 in s:
                    for i5 in s:
                        s2=i1+i2+i3+i4+i5
                        if s2.count('1')==1 and s2.count('2')==1 and s2.count('3')==1 and s2.count('4')==1 and s2.count('5')==1:
                            k+=1

print(k)
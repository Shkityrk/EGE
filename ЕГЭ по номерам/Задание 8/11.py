k=0
for n in range(100,1000000):
    s=str(oct(n)[2:])
    if s.count('4')==2 and len(s)==5:
        if all((x+'4' not in s) and ('4'+x not in s) for x in '13579'):
            k+=1
            print(s)
print(k)
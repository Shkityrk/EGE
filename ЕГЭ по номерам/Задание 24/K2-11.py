a=[s[:-1] for s in open('K2/24-11.txt').readlines()]
k=m=0
for s in a:
    for i in range(len(s)-3):
        if s[i]=='K' and s[i+2]+s[i+3]=='GE':
            k+=1
    if k!=0:
        m+=1
        k=0
print(m)
s=open('data/24-j5.txt').readline()
c=0
for i in range(len(s)-5):
    if s[i]=='O' and s[i+1]=='C' and  s[i+2]=='K':
        if s[i-2]!='S' and s[i-1]!='T' and i<2 or(s[i-2:i]!='ST'):
            c+=1
print(c)
s=open('K2/24-5.txt').readline()

c=0
for i in range(len(s)-2):
    if s[i]=='X' and s[i+1]=='I' and s[i+2]=='X':
        c+=1
print(c)
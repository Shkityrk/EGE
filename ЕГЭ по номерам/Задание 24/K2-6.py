s=open('K2/24-6.txt').readline()
c=0
for i in range(len(s)-3):
    if s[i]+s[i+1]+s[i+2]+s[i+3]=='XXXX':c+=1
print(c)
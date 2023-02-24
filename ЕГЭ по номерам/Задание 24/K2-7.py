s=open('K2/24-7.txt').readline()
c=0
for i in range(len(s)-3):
    if (s[i]=='G') and (s[i+2]+s[i+3]=='ME'):
        c+=1
print(c)

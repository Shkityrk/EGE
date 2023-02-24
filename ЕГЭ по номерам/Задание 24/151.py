s=open('data/24-j9.txt').readline()
c=0
for i in range(len(s)-5):
    if s[i]==s[i+4] and s[i+1]==s[i+3]:c+=1
print(c)
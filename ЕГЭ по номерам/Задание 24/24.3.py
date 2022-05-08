f=open('j3.txt')
s=f.readline()
tik=0
tok=0
for i in range(2, len(s)):
    if s[i-2]=='T' and s[i-1]=='I' and s[i]=='K':
        tik +=1
    if s[i-2]=='T' and s[i-1]=='O' and s[i]=='K':
        tok +=1
print (tik+tok)
print (sum(tik,tok))
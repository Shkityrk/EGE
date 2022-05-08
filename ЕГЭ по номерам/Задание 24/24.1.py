f = open('j5.txt')
s=f.readline()
count=0
for i in range (2, len(s)):
    if s[i-2]=='T' and s[i-1]=='O' and s[i]=='K':
        if s[i-5]!='T' and s[i-4]!='O':
            count += 1
print (count)
l=[0 for x in range(500)]

s=open('data/24-s2.txt').readline()
for i in range(0,len(s)-2):
    if s[i]=='A' and s[i+2]=='C':
        l[ord(s[i+1])]+=1
m=max(l)
print(l)
print(chr(m))
print(m)
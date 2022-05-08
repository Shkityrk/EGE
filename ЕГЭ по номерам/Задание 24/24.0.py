
f=open("24-19.txt")
s=f.read()


l=[0 for _ in range(65, 91)] #[0]==B,
for i in range(1,len(s)-1):
    if s[i-1]=='A' :
        l[ord(s[i])-65]+=1

print(chr(l.index(max(l))+65))
'''
m='B'
l[ord(m)-65]+=1'''


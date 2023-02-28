
s=open('24/24var09-13.txt').readline()
'''
c=m=0
l=''
for i in range(len(s)):
    l+=s[i]
    if l.count('Z')<=2:
        m=max(len(l),m)
    else:
        l=''
print(m)
'''
m=0
s=s.split('Z')
for i in range(len(s)-2):
    l=s[i]+'Z'+s[i+1]+'Z'+s[i+2]

    m=max(len(l),m)
print(m)
    

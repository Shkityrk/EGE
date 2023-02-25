s=open('24/24var09-13.txt').readline()
c=m=0
l=''
for i in range(len(s)):
    l+=s[i]
    if l.count('Z')<=1:
        m=max(len(l),m)
    if l.count('Z') > 1:
        l=''
print(m)
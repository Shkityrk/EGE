a=[0 for _ in range (100)]
f=open("s2.txt")
s=f.readline()
mx=0
otv ='*'

for i in range(0, len(s)-1):
    if s[i]=='A':
        a[ord(s[i+1])]+=1
        if a[ord(s[i+1])]>mx:
            mx=a[ord(s[i+1])]
            otv=s[i+1]
print (otv, mx) 
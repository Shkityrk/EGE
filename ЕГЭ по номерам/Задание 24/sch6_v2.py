f=open('schelchok/6__1vq2h.txt')
s=[str(x) for x in f.readlines()]
k=0
strin=''
maxx=0

for i in s:
    if i.count('O')>maxx:
        strin=i
        maxx=i.count('O')
a=[0]*1000
sogl='WRTPSDFGHJKLZXCVBNM'
for i in range(2,len(strin)):
    if strin[i-2] in sogl and strin[i]=='O':
        ltr=strin[i-1]
        a[ord(ltr)]+=1
for i in range(len(a)):
    print(chr(i),a[i])
'''ans=0
for i in s:
    ans+=i.count('J')
print(ans)'''
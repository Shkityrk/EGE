s=open('schelchok/5__1vv4o.txt').readline()
k=0
last=0
for i in range(2,len(s)):
    if ord(s[i-1])>ord(s[i-2]) and ord(s[i-1])>ord(s[i]):
        k+=1
        last=i-2
print(k,last)
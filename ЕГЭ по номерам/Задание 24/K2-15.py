s=open('K2/24-15.txt').readline()
a=[0 for _ in range(300)]

for i in range(len(s)):
    a[ord(s[i])]+=1

m=max(a)
for i in range(len(a)):
    if a[i]==m:
        print(chr(i),m)


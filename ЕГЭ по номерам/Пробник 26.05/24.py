f=open("24.txt")
s=f.readline()
a=[0 for n in range(65,91)]
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        a[ord(s[i+1])-65]+=1
mx=0
mx_index=0
print(a)
print([chr(l) for l in range(65,91)])
for n in range(len(a)):
    if a[n]>mx:
        mx=a[n]
        mx_index=n
print(chr(a[mx_index]))

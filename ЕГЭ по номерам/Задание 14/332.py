n=19**81+23**709-4
s=str()
a=[]
while n!=0:
    s+=str(n%9)
    n//=9
s=s[::-1]
for i in range(1,len(s)):
    if s[i-1]=='8' and s[i] not in '08' :
        a.append(s[i-1]+s[i])
print(a)
print(len(a))
n=343**1515-6*49**1520+5*49**1510-1550
s=str()
while n!=0:
    s+=str(n%7)
    n//=7
s=s[::-1]
while s[0]=='0':
    s=s[1:]
print(s.count('0'))
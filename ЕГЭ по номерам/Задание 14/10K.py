n=5*216**1156-4*36**1147+6**1153-875
s=''
while n!=0:
    s=s+str(n%6)
    n//=6
print(s.count('5')-s.count('0'))
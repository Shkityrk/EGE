n=60
b=bin(n)[2:]
s=str(b)
if s.count('1')%3==0:s=s+s[:2]
else:
    ost=bin(3*(s.count('1')%3))[2:]
    s=str(ost)+s
r=int(s,2)
print(r)
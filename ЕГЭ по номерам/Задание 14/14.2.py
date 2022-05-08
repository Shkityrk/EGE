a= 216**6+216**4-6**14-24
n0=0
n1=0
n2=0
n3=0
n4=0
n5=0

while a !=0:
    if a%6==0:
        n0=n0+1
    if a % 6 == 1:
        n1 = n1 + 1
    if a%6==2:
        n2=n2+1
    if a%6==3:
        n3=n3+1
    if a%6==4:
        n4=n4+1
    if a%6==5:
        n5=n5+1
    a//6
print ( n0,n1,n2,n3,n4,n5)
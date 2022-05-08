start ,end = 4986, 32599
def kol_divs(n):
    num=0
    for d in range(1,n//2+1):
        if n%d==0:
            num+=1
    return num
n=0
for i in range(start,end+1):
    if kol_divs(i)==3:
        n+=i
print(n)
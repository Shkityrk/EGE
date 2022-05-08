start, end = 33_333, 55_555
def is_true(i):
    return n[0]%2!=0 and n[1]%2!=0 and n[2]%2==0 and n[3]%2!=0 and n[4]%2==0 and n%6!=0 and n%7!=0 and n%8!=0


mx=-1
mn=1000000
num=0

for i in range(start,end+1):
    n=list(map(int, str(i)))
    if is_true(i):
        num+=1
        if i>mx:
            mx=i
        if i<mn:
            mn=i
print(num, mx-mn)
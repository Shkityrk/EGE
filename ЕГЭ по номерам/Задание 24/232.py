s=open('data/24-232.txt').readline()
s=s.split('0')
m=0
n=0
for c in s:
    if sum(map(int,c))%5==0:
        if len(c)>m:
            m=len(c)
            n=sum(map(int,c))
print(n)
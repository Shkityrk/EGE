import time
f=open('files_compege/test-2.txt')
n=int(f.readline())
k=int(f.readline())


number=[[] for _ in range(100000000)]

for i in range(n):
    num,t,znach=map(int,f.readline().split())
    number[num].append([t, znach])
number=[x for x in number if x!=[]]
razn=0
print(len(number))
for x in number:
    x.sort()
    for i in range(len(x)):
        for j in range(len(x)):
            if x[j][0]-x[i][0]>=k:
                n1=int(x[j][1])
                n2=int(x[i][1])
                razn=max(razn, abs(n2-n1))


print(razn)
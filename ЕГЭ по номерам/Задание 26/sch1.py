f=open('files_kompege/26_1__1vv2w.txt')
A,C,B=f.readline().split()#кол-ов пунктов, места, пассажиры
A=int(A)
C=int(C)
B=int(B)
count=0

a=[]
for i in range(B):
    st,end=map(int,f.readline().split())
    a.append([st,end])
a.sort(key=lambda x:(x[0],-x[1]))
per=[[0]*(A+1) for _ in range(C)]

for st,fn in a:
    for i in range(C):
        if per[i][st]==0:
            count+=1
            for j in range(st,fn):
                per[i][j]=1
            break
c_per=0
for p in range(1,A+1):
    if all(per[i][p]==1 for i in range(C)):
        c_per+=1
print(count,c_per)
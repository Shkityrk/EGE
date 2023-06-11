f=open('files_compege/27B_2761.txt')
n=int(f.readline())
q=[int(f.readline()) for i in range(5)]
k=[[0]*13 for _ in range(2)]
count=0
for i in range(n-5):
    x=int(f.readline())
    ost=x%13
    if x%2==0:count+=k[0][ost]+k[1][ost]
    if x%2!=0:count+=k[0][ost]

    k[q[0]%2][q[0]%13]+=1

    q.append(x)
    q.pop(0)

print(count)
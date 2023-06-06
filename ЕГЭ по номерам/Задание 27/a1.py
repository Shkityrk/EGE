f=open('files/27_B_8513.txt')
k=int(f.readline())
n=int(f.readline())
s=[]
for i in range(n):
    s.append([i,int(f.readline())])
s.sort(key = lambda row: row[1])

s=s[::-1]
for i in range(n):
    for j in range(i,n):
        a0=s[i][0]
        a1=s[j][0]
        ind=[a0,a1]
        ind.sort()
        if ind[1]-ind[0]>=k:
            print(s[i][1]+s[j][1])
            exit()




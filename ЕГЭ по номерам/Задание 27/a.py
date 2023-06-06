f=open('files/27b_8483.txt')
n=int(f.readline())
k=int(f.readline())
s=[]
for i in range(n):
    s.append([i,int(f.readline())])
s.sort(key = lambda row: row[1])

s=s[::-1]
for i in range(n):
    for j in range(i,n):
        for l in range(j, n):
            a0=s[i][0]
            a1=s[j][0]
            a2=s[l][0]
            ind=[a0,a1,a2]
            ind.sort()
            if ind[1]-ind[0]>=k and ind[2]-ind[1]>=k:
                print(s[i][1]+s[j][1]+s[l][1])
                break



f=open('files_compege/27B_2752.txt')

n=int(f.readline())
a=[int(f.readline()) for i in range(n)]
countA=countB=0
for i in range(n):
    for j in range(i+1,n):
        if a[i]*a[j]%10==3 and j-i>=6 :countA+=1
print(countA)

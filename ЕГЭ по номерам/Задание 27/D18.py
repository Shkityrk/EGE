f=open('files_compege/27B_2759.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]

k=[0]*134
count=0
for i in range(n):
    x=a[i]
    if x<134:
        for j in range(x+1,134):
            if x+j<=134:count+=k[j]
        k[x]+=1

print(count)
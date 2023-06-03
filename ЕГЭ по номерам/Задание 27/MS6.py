f=open('files_compege/27-B_2949.txt')
n=int(f.readline())
k=[0]*10

for i in range(n):
    x=int(f.readline())
    k1=k.copy()
    for i in range(10):
        k1[(i+x)%10]+=k[i]
    k1[x%10]+=1
    k=k1
print(k[5])
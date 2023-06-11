f=open('files_compege/27B_2726.txt')
n=int(f.readline())
print(n)
a0=[]
a1=[]
for i in range(n):
    x=int(f.readline())
    if x%2==0:a0.append(x)
    else: a1.append(x)
print(max(a0)+max(a1))


from itertools import *
f=open('files_compege/27B_2719.txt')
n=int(f.readline())
k0=k1=0
for i in range(n):
    x=int(f.readline())
    if x%2==0:k0+=1
    else:k1+=1
print(k0*(k0-1)//2+k1*(k1-1)//2)
f=open('files_compege/27B_2722.txt')
n=int(f.readline())

k5_0,k5_1,k_0,k_1=0,0,0,0

for i in range(n):
    x=int(f.readline())
    if x%5==0 and x%2==0:k5_0+=1
    if x % 5 == 0 and x % 2 != 0: k5_1 += 1

    if x % 5 != 0 and x % 2 == 0: k_0 += 1
    if x % 5 != 0 and x % 2 != 0: k_1 += 1
print( k5_0*k5_1 + k5_0*k_1 + k_0*k5_1 )
f=open('files_compege/27B_2751.txt')
n=int(f.readline())
k=5
a=[int(f.readline()) for x in range(n)]
countA=countB=0


k_0=k_1=k_0_13=k_1_13=0
for i in range(k,n):
    if a[i - k] % 2 == 0 and a[i - k] % 13 == 0: k_0_13 += 1
    if a[i - k] % 2 == 0 and a[i - k] % 13 != 0: k_0 += 1
    if a[i - k] % 2 != 0 and a[i - k] % 13 == 0: k_1_13 += 1
    if a[i - k] % 2 != 0 and a[i - k] % 13 != 0: k_1 += 1

    if a[i] % 2 == 0 and a[i] % 13 == 0: countB+=k_1_13+k_1
    if a[i] % 2 == 0 and a[i] % 13 != 0: countB +=k_1_13
    if a[i] % 2 != 0 and a[i] % 13 == 0: countB +=k_0+k_0_13
    if a[i] % 2 != 0 and a[i] % 13 != 0: countB +=k_0_13

print(countB)
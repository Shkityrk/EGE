f=open('files_compege/27B_2721.txt')
n=int(f.readline())
k65=k13=k5=k=0
for i in range(n):
    x=int(f.readline())
    if x%65==0:k65+=1
    elif x%13==0:k13+=1
    elif x % 5 == 0:
        k5 += 1
    else:k+=1
print(k65*(k65-1)//2 + k65*(n-k65) + k13*k5 )
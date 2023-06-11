f=open('files_compege/27B_2720.txt')
n=int(f.readline())

k7=k=0

for i in range(n):
    x=int(f.readline())
    if x%7==0:k7+=1
    else:k+=1

print(k7*(k7-1)//2 + k7*k)
f=open('files_compege/27B_2733.txt')
n=int(f.readline())

max_50000=[0]*80
min_50000=[0]*80

for i in range(n):
    x=int(f.readline())
    if x>50000 : max_50000[x%80]+=1
    else:min_50000[x%80]+=1

count=0
count+=max_50000[0]*(max_50000[0]-1)//2 + max_50000[40]* (max_50000[40]-1)//2

for i in range(1,40):
    count+=max_50000[i]*max_50000[80-i]

count+=max_50000[0]*min_50000[0] +max_50000[40]*min_50000[40]
for i in range(1,40):
    count+=max_50000[i]*min_50000[80-i]
    count += min_50000[i] * max_50000[80 - i]
print(count)
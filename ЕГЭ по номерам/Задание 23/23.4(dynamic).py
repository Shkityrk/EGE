a=[0]*100
a[2]=1
for i in range(2,9):
    if i+1<=9: a[i+1]+=a[i]
    if i +3 <= 9: a[i + 3] += a[i]
for i in range(9,18):
    if i==14: a[i]=0;
    if i+1<=18: a[i+1]+=a[i];
    if i +3 <= 18: a[i + 3] += a[i];
print(a[18]);
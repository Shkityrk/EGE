f=open('kompege/17_2016.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(len(a)):
    if a[i]%13==7 and a[i]%7!=0 and a[i]%11!=0:ans.append(a[i])
print(max(ans)-min(ans),len(ans))
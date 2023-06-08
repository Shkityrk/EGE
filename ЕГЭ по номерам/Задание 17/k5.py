f=open('kompege/17_2016.txt')
a=[int(x) for x in f.readlines()]
ans=[]

for i in range(len(a)):
    if a[i]%16==11 and a[i]%7==0 and a[i]%6!=0 and a[i]%13!=0 and a[i]%19!=0:ans.append(a[i])
print(sum(ans),len(ans))
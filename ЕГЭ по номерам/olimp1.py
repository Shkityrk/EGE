def split(x):
    l=[]
    for char in x:
        l.append(char)
    return l

s=str(input())
if len(s)==1:
    print('YES')
    print(s)
else:
    flag=None
    li=split(s)
    for i in range(((len(li)//2))):
        if li[i]==li[len(li)-i-1]:
            flag=True
        elif li[i]!=li[len(li)-i-1]:
            flag = False
            if flag==False:
                print('NO')
                break
    if flag==True:
        for i in range(len(li)):
            if li[i]=='?':
                li[i]='a'
        print('YES')
        print(*li,sep='')

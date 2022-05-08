start=26868
end=56868

def prost(x):
    for j in range(1,int(x**0.5)+1):
        if x%j==0:
            return 0
    return 1

mxdel=-1
for i in range(start,end+1):
    c=0
    for j in range(2,i):
        if i%j==0:
            if prost(j)==1:
                c+=1
                mxdel=j
    if c>=6:
        print(i,mxdel)

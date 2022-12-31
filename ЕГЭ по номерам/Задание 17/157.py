with open("data/17-1.txt") as f:
    a=[int(x) for x in f.readlines()]

l=k=0
mx_len=1
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        mx_len+=1
    elif mx_len>=l:
        l=mx_len
        mx_len=1
    else:mx_len=1
mx_len=1
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        mx_len+=1
    elif mx_len==l:
        k+=1
        mx_len=1
    else:mx_len=1
print(l,k)

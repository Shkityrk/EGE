with open("data/17-1.txt") as f:
    a=[int(x) for x in f.readlines()]
l=0
mx_len=0
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        mx_len+=1
        l=max(mx_len,l)
    else:mx_len=0


print(l)
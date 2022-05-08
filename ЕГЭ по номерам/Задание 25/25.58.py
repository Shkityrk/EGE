start, end = 87921, 88187

def num(n):
    s=[]
    while n!=0:
        s.append(n%10)
        n=n//10

    return s

def pr(n):
    p=1
    for l in n:
        p=p*l

    return p

for i in range(start,end+1):
    nums = num(i)
    su = sum(nums)
    p = pr(nums)
    if su%14==0 and p%18==0 and p!=0:
        print(su, p)
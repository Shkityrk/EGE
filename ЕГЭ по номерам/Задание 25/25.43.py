start ,end = 2031, 14312
def num_system(n):
    s=[]
    while n!=0:
        s.append(n%11)
        n=n//11
    return s
for i in range(start,end+1):
    list = num_system(i)
    if 2 not in list:
        print(i)
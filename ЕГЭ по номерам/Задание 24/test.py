f=open('data/file_4.txt').readlines()
a=[]
for s in f:
    t=[int(x) for x in s.split()]
    a.append(sum(t))
print(sum(a))
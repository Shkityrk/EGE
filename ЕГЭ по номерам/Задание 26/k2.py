f=open('files_kompege/26_838.txt')
n=int(f.readline())
a=[int(x) for x in f.readlines()]
d1=[]
d2=[]
a.sort()

while len(a)>0:
    d1+=[a.pop(-1)]
    while sum(d2)<=sum(d1):d2+=[a.pop(0)]
print(len(d1),len(d2))
a=[int(x) for x in open("data/17-4.txt")]
l=[]
for i in range(len(a)):
    if a[i]%16==9 and a[i]%25==6:l.append(a[i])
print( max(l) , sum(l))
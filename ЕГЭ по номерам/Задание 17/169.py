a=[int(x) for x in open("data/17-4.txt")]
l=[]
for i in range(len(a)):
    if a[i]%3==0 and all(a[i]%x!=0 for x in [7,17,19,27]):l.append(a[i])
print(len(l),max(l))
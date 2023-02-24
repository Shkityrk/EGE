s=open('data/k7/k7-m22.txt').readline()
index=-1
c=0
r=0
for i in range(len(s)-2):
    index+=1
    if s[i]>s[i+1]>s[i+2]:
        r=index
        c+=1
print(c,index)
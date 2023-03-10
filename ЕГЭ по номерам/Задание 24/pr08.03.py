a=open('data/24-212.txt').readline()
a=a.replace('O','A').replace('C','B').replace('D','B')
a=a.replace('AB','*')
k=m=0
for i in range(len(a)):
    if a[i]=='*':
        k+=1
        m=max(k,m)
    else:k=0
print(m)
a=open('schelchok/2__1vf5w.txt').readline()
k=1
mx=0
for i in range(1,len(a)):
    if a[i-1]==a[i]:
        k+=1
        mx=max(mx,k)
    else:k=1
print(mx)
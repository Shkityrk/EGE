r=[1,2,3,2,1]
for x in range(0,int(len(r)**0.5)):
    if r[x]==r[len(r)-1-x]:
        print(r[x], r[len(r)-1-x])
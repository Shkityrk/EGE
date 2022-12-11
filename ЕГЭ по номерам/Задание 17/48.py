mx=0
l=1
for n in range(1985, 8529):
    if n%10+n%100//10==6 and all(n%x!=0 for x in (2,4,47)):
        mx=max(mx,n)
        l*=n
print(mx, l%1000)
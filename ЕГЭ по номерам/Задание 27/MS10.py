f=open('files_compege/27B_2904.txt')
n=int(f.readline())
s=[[0,0]]
ans=[]
for i in range(n):
    x=int(f.readline())
    s=[[a+x,b+1] for a,b in s]+[[x,1]]
    s={x[0]%2077:x for x in sorted(s)}
    if 0 in s:ans.append(s[0])
    s=s.values()
ans.sort()
print(ans)
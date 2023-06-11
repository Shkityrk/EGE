f=open('files_compege/27-A_2949.txt')
n=int(f.readline())
s=[0]

for i in range(n):
    x=int(f.readline())

    s=s+[x]+ [a+x for a in s]
    s=list({x%10:x for x in sorted(s)} )
f=open("s1-2.txt")
s=f.readline()
mina=10000000000

for s in f:
    cT=s.count('T')
    if cT<mina:
        mina=cT
        mb=-1
        b='*'
        for i in range(ord('A'), ord('Z')+1):
            if s.count(chr(i))>mb:
                mb=s.count(chr(i))
                b=chr(i)
print(b)
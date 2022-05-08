f=open('j2.txt')
s=f.readline()

max=-1
c=0
for i in range (1, len(s)):
    if [i-1]==[i]:
        c = 0

    else:
        c += 1
        if c > max:
            max = c
print (max)
s=open('data/24-1.txt').readline()
a=[]
c=''

for i in range(len(s)-1):
    if s[i] in '1234567890': c+=s[i]
    else:
        if c!='':
            a.append(int(c))
            c=''
f=[s for s in a if s%2==0]
print(max(f))
s=open('data/24-5.txt').readline()

c=0
for i in range(len(s)):
    if s[i]==')':
        c+=1
        if c==10000:
            print(i+1)
            break
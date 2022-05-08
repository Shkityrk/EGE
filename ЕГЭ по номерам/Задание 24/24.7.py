f=open('5 со скобками-2.txt')
s=f.readline()
count =0
for i in range (1,len (s)):
    if s[i-1]=='(' and s[i]==')':
        count +=1
        if count ==10000:
            print (i)
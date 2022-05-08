f=open ('5 со скобками-2.txt')
s=f.readline()
count =0
kol=1

for i in range (0, len (s)):
    if s[i]==')':
        count +=1
        if count ==1000:
            print (i+1)






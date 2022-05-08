f=open('j9.txt')
s=f.readline()
count=0
for i in range (4,len(s)):
    if s[i-4]==s[i] and s[i-3]==s[-1]:
        count+=1
print (count)
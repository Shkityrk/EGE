s=open('data/k7/k7c-5.txt').readline()
k=0
for i in range(len(s)-5):
    if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i+3] and s[i+3]!=s[i+4]:k+=1
print(k)
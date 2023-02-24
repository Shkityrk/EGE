s=open('K2/24-14.txt').readline()
k=0
for i in range(len(s)-4):
    if s[i]==s[i+4] and s[i+1]==s[i+3]:
        k+=1
print(k)
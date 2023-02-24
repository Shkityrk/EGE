s=open('K2/24-8.txt').readline()

k=0
for i in range(len(s)-4):
    if s[i]== 'A' and s[i+2]=='A' and s[i+4]=='A':k+=1
print(k)
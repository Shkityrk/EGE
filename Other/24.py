s=open('24__1vpyb.txt').readline()
n1='QWERTYUIOPASDFGHJKLZXCVBNM'
n2='qwertyuiopasdfghjklzxcvbnm'
k=0
for i in range(len(n1)):
    if n1[i] not in s and n2[i] not in s:
        k+=1
print(k)
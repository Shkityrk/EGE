f = open("ЕГЭ-1.txt")
s=[]
kol=0
mx_sum=0
for n in f:
    s.append(int(n[:-1]))
for i in range(1,len(s)-1):
    su=(s[i-1]+s[i])
    if su%9==0:
        kol+=1
        if su>mx_sum:
            mx_sum=su
print(kol, mx_sum)
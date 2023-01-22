s=[int(x) for x in open("18-k3.txt")]
kol=0
for i in range(len(s)):
    for k in range(1,6):
        if i+k<len(s) and (s[i]+s[i+k])<100:
            kol+=1
            print(kol)

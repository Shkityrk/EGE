s=[int(x) for x in open("18-k3.txt")]
l=0

for i in range(len(s)):
    for k in range(1,7):
        if i+k<len(s):
            if (s[i]+s[i+k])%2==0:l+=1
print(l)
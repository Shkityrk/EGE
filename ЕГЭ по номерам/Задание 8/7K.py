from itertools import permutations
k=0
sogl=['Б','К','Л','Н']
gl=['А','И','У','О']
for x in permutations('АБИКОЛУН'):
    s=''.join(x)
    f=1
    for i in range(1,len(s)):
        if (s[i-1] in sogl and s[i] in sogl) or(s[i-1] in gl and s[i] in gl):
            f=0
    if f==1:k+=1
print(k)
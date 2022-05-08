k3='3'*17
k4='4'*23
k5='5'*29
s='3'*17+'4'*23+'5'*29
while '43' in s or '53' in s :
    if '43' in s:
        s=s.replace ('43', '33', 1)
    else:
        s = s.replace('53', '433', 1)
n1= s.count('3')



print (max(n1, n2,n3))
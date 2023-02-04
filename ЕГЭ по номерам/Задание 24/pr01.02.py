s=open("data/24.txt").readline()
mx=0
l=1
for i in range(3, len(s)):
    if s[i-3] in 'CDF' and s[i-2] in 'AO' and s[i-1] in 'CDF' and s[i] in 'AO':
        l = 0
    else:
        l += 1
        mx = max(l, mx)

print(mx)
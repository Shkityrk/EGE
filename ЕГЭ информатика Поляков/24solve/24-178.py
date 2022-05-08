# Автор: В. Якшигулов

f = open('24-178.txt')
s = f.readline().strip()
s = s + s
cur = mx = 1
for i in range(1, len(s)):
    if s[i-1] <= s[i]:
        cur += 1
        mx = max(mx, cur)
    else:
        cur = 1
print(mx)
f.close()

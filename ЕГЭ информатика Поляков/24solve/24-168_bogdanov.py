# Автор: А. Богданов
# Видеоразбор: https://youtu.be/qSvL8y8UOAI

s = open('24-168.txt').readline()
x = y = z = m = 0
for i in range(1,len(s)):
  m = max(m,i-x)
  if s[i-1]>s[i]:
    x = y = z = i
  elif s[i-1]<s[i]:
    x,y,z = y,z,i
print(m)

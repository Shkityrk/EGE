# Автор: А. Богданов

with open('24-180.txt') as F:
  a = F.readline().strip()

k = [0]*4;
kMax = 0;
for i in range(len(a)-3):
  (h10, h1, m10, m1) = map( int, a[i:i+4] )
  if h10*10+h1 < 24 and m10*10+m1 < 60:
    k[i%4] += 1
    kMax = max(kMax, k[i%4])
  else:
    k[i%4] = 0

print( kMax )

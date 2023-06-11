with open('27-154b.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

tail = [ [0]*K for k in range(K) ]
count = 0
for j in range(N):
  for rji in range(K): # возможные остатки (j - i) % K
    ri = (K + j - rji) % K # остаток индекса предыдущих парных элементов
    rPair = (K + ri - data[j]) % K # остаток предыдущих парных элементов
    count +=  tail[rPair][rji]
  tail[data[j]%K][j%K] += 1

print( count )
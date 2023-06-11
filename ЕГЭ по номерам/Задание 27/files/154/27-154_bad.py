with open('27-154a.txt') as F:
  N, K = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

count = 0
for i in range(N-1):
  for j in range(i+1,N):
    if (data[i]+data[j]) % K == (j - i) % K:
      #print( i, j, data[i], data[j] )
      count += 1

print( count )
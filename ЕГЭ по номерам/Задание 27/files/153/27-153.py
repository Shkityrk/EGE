with open('27-153b.txt') as F:
  K, N = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

tail = [None]*K
totalSum = maxSum = 0
for i in range(N-1):
  totalSum += data[i]
  r = totalSum % K
  if tail[r] is None:
    tail[r] = data[i]
  else:
    maxSum = max( tail[r]+data[i+1], maxSum )
    tail[r] = max( data[i], tail[r] )

print( maxSum )


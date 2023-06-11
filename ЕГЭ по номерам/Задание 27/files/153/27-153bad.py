with open('27-153a.txt') as F:
  K, N = map( int, F.readline().split() )
  data = [ int(s) for s in F ]

maxSum = 0
for i in range(N-1):
  for j in range(i+2,N):
    s = sum( data[i+1:j] )
    if s % K == 0 and data[i]+data[j] > maxSum:
       #print( data[i], data[j], s)
       maxSum = data[i] + data[j]

print( maxSum )


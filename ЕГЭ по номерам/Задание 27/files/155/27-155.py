with open('27-155a.txt') as F:
  N, D, T = map( int, F.readline().split() )
  data = [int(F.readline()) for _ in range(N)]

count = 0
countND = 0
Q = [0]
for i in range(N):
  if data[i] % D != 0:
    if len(Q) > T:
      count += Q[T-1] - Q[T]
    countND += 1
  else:
    Q.insert( 0, countND )

print( count )
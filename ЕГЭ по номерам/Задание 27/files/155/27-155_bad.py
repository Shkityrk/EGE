with open('27-155a.txt') as F:
  N, D, T = map( int, F.readline().split() )
  data = [int(F.readline()) for _ in range(N)]

count = 0
for i in range(N):
  if data[i] % D != 0:
    countD = 0
    for j in range(i+1, N):
      if data[j] % D == 0:
        countD += 1
        if countD > T: break
      else:
        if countD == T:
          count += 1

print( count )
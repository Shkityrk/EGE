with open('27-152a.txt') as F:
   N = int(F.readline())
   data = []
   for _ in range(N):
      data.append( int(F.readline()) )

D = 5
count = 0
for i in range(N):
  for j in range(i+1,N):
    p = data[i]*data[j]
    if p % 10**D == 0 and p % 10**(D+1) != 0:
      # print( (data[i], data[j]), end=", " )
      count += 1

print( count )

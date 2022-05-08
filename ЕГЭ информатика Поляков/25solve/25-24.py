from math import sqrt

start, end = 11275, 16328

qStart = int(sqrt(start))
qEnd = int(sqrt(end))+1
for q in range( qStart, qEnd+1 ):
  n = q*q
  if not (start <= n <= end): continue
  a = [q] # массив для хранения делителей
  for d in range(1, q):
    if n % d == 0:
      a = a + [d, n//d]
      if len(a) > 5: break
  if len(a) == 5:
    print( *sorted(a) )

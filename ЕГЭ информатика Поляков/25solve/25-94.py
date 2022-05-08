start, end = 3159, 31584

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

s = 0
for x in range( start, end+1 ):
  if isPrime(x):
    s += sum( map(int, str(x)) )

print(s)

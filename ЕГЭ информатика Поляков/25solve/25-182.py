def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

L1, L = 2, 1
n = 2
while L < 10**6:
  L1, L, n = L, L1+L, n+1
while L < 10**9:
  L1, L, n = L, L1+L, n+1
  if isPrime(L):
    print( n, L )


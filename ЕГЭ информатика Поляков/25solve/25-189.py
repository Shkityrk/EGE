def allDivs(n):
  q = round(n**0.5)
  divs = [q] if n % q == 0 else []
  for d in range(2,q):
    if n % d == 0:
      divs += [d, n//d]
  return sorted(divs)

def isPrime( x ):
  if x <= 1: return False
  d = 2
  while d*d <= x:
    if x % d == 0:
      return False
    d += 1
  return True

MIN = 10000000
count = 0
x = MIN + 1
while count < 5:
  divs = allDivs(x)
  if len(divs) >= 3:
    S = divs[-1]+divs[-2]+divs[-3]
    if isPrime(S):
      print( S, divs, x ) #, divs )
      count += 1
  x += 1
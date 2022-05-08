def allDivs(n):
  q = round(n**0.5)
  divs = [q] if n % q == 0 else []
  for d in range(2,q):
    if n % d == 0:
      divs += [d, n//d]
  return sorted(divs)

def isDescending( x ):
  prev = 10
  while x:
    d = x % 10
    if d > prev: return False
    x //= 10
    prev = d
  return True

MIN = 10000000
count = 0
x = MIN + 1
while count < 5:
  divs = allDivs(x)
  if len(divs) >= 3:
    S = divs[-1]+divs[-2]+divs[-3]
    if isDescending(S):
      print( S, divs, x ) #, divs )
      count += 1
  x += 1
def isValid( n ):
  return all( c in '13579' for c in str(n) )

def allDivs( n ):
  q = round( n**0.5 )
  divs = [q] if n % q == 0 else []
  for d in range(2,q):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted(divs)

n = 300000000-1
count = 0
k = 5
pairs = []
while count < 5:
  divs = [d for d in allDivs(n) if isValid(d)]
  if len(divs) >= k:
    pairs.append( (divs[-k], len(divs)) )
    count += 1
  n -= 1

for p in pairs[::-1]:
  print( *p )
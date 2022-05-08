def allDivs( n ):
  q = round( n**0.5 )
  divs = [q] if n % q == 0 else []
  for d in range(2,q):
    if n % d == 0:
      divs.extend( [d, n//d] )
  return sorted(divs)

n = 400000000 + 1
count = 0
k = 7
while count < 5:
  divs = allDivs(n)
  if len(divs) >= k:
    print( divs[-k], len(divs) )
    count += 1
  n += 1
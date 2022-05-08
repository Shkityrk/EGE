def allDivs(n):
  q = round(n**0.5)
  divs = [q] if n % q == 0 else []
  for d in range(2,q):
    if n % d == 0:
      divs += [d, n//d]
  return sorted(divs)

MIN = 10000000
count = 0
x = MIN + 1
while count < 5:
  divs = allDivs(x)
  if len(divs) >= 2:
    S = divs[-1]+divs[-2]
    if S < 100000 and S % 31 == 0:
      print( S, divs, x ) #, divs )
      count += 1
  x += 1
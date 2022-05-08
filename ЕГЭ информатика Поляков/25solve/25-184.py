def allDivs(n):
  q = round(n**0.5)
  divs = [q] if n % q == 0 else []
  for d in range(2,q):
    if n % d == 0:
      divs += [d, n//d]
  return sorted(divs)

MIN = 300000000
count = 0
x = MIN + 1
while count < 5:
  divs = allDivs(x)
  if len(divs) >= 5:
    M = divs[0]*divs[1]*divs[2]*divs[3]*divs[4]
    if M < x and M % 100 == 31:
      print( M, divs[4] ) #, divs )
      count += 1
  x += 1
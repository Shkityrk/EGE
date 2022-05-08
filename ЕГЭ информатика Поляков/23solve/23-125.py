def simple(x):
      k=0
      for i in range (1,x+1):
           if x%i==0:
                k+=1
      if k==2:
           return 1
      else:
           return 0

def nextPrime( x ):
  x += 1
  while not simple(x):
     x += 1
  return(x)

def rec( x, y ):
   if x == 33: return 0
   if x > y: return 0
   if x == y: return 1
   return rec(x+2, y) + rec(nextPrime(x), y)

a = [0] + [1]*45
for i in range(2, 46):
  a[i] = a[i-2]
  if simple(i):
    k = i - 1
    print(i, "+", end=" ")
    while k > 0 and not simple(k):
      a[i] += a[k]
      print(k, end=" ")
      k -= 1
    if k > 0:
        a[i] += a[k]
        print( k, end=" " )
    print()
  if i == 33: a[i] = 0
  if i == 14:
    for k in range(1,14):
        a[k] = 0

print( "Динамическое программирование" )
print(a[45])

print( "Рекурсия" )
print( rec(2,14) * rec(14,45) )

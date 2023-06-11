with open('27-152b.txt') as F:
   N = int(F.readline())
   data = []
   for _ in range(N):
      data.append( int(F.readline()) )

def extract25( n ):
  n2 = n5 = 0
  while n % 2 == 0:
    n2, n = n2+1, n // 2
  while n % 5 == 0:
    n5, n = n5+1, n // 5
  return n2, n5

D = 5
s25 = {}
count = 0
for n in data:
  n2, n5 = extract25( n )
  count += sum( s25[(n2a, n5a)]
                for n2a, n5a in s25
                if min(n2+n2a, n5+n5a) == D )
  s25[(n2, n5)] = s25.get( (n2, n5), 0 ) + 1

print( count )

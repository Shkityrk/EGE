Ncmd = 8

def rec( n, remains, target, way ):
  way += [n]
  if remains == 0:
    if n == target:
      print( way )
      return 1
    return 0
  return rec( n+1, remains-1, target, way[:] ) + \
         rec( n+5, remains-1, target, way[:] ) + \
         rec( n*3, remains-1, target, way[:] )

count = 0
for target in range(1000, 1024+1):
  if rec(1, Ncmd, target, [] ) > 0:
    count += 1

print( count )
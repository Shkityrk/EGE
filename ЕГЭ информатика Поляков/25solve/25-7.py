start, end = 113012, 113061

for n in range( start, end+1 ):
  a = [] # массив для хранения делителей
  for d in range(1,n+1):
    if n % d == 0:
      a.append(d)
      if len(a) > 4: break
  if len(a) == 4:
    print( *a )

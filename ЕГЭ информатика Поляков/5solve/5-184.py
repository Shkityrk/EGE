def alg( x ):
  s = "{:08b}".format(x-1)
  s1 = ""
  doInversion = True
  for c in reversed(s):
    if c == '1': s1 = '0' + s1
    else:        s1 = '1' + s1
  return int(s1,2)

for i in range(1, 256):
  print( i, alg(i) )
  if alg(i) == 18:
    break

for s in range (1,1000,1):
  n = 1
  max=0
  while s > 200:
    s = s - 15
    n = n + 3
  print(n)
  if n ==46:
    if s>max:
      max=s
    print (s)
print ("Максимальное s", max)
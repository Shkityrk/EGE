from random import randint
with open('27-152b.txt', "w") as F:
   N = 83256
   print( N, file = F )
   for _ in range(N):
      x = randint(100000000, 1000000000)
      print( x, file = F )
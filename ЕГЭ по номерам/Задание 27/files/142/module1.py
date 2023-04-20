with open('27-142b.txt') as F:
  with open('27-142bb.txt', "w") as Fout:
    N, K, M = map(int, F.readline().split())
    N = N // 20
    print(N, K, M, file=Fout)
    for i in range(N):
      p, x = map(int, F.readline().split())
      print( p, x//2, file = Fout )
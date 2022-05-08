target = 'XYZ'
Lmax = 0
with open("24-171.txt") as F:
  while True:
    s = F.readline().strip()
    if not s: break
    L = 0
    state = 0 # 'X'
    for i in range(len(s)):
      #print( s[i], state )
      if s[i] == target[state]:
        L += 1
        Lmax = max( L, Lmax )
        state = (state + 1) % 3
      else:
        if s[i] in target:
          L = 1
          state = target.index(s[i])
          state = (state + 1) % 3
        else:
          L = 0
      #print( L, Lmax, state )

print( Lmax )
# Автор: А. Кузнецов

from string import ascii_uppercase

maximum = []

def f(n):
  global maximum
  for nn in ascii_uppercase:
    sp = [index for index, sim in enumerate(n)
                if sim == nn]
    if len(sp) >= 2:
      for r in range(len(sp)-1):
        if sp[r+1] > sp[r]+1:
          maximum.append(sp[r+1] - sp[r])

for s in open('24-174.txt'):
  s = s.strip()
  if s.count('R') < 30:
    f(s)

print( max(maximum), len(maximum) )
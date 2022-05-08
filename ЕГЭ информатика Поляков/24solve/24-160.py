sMinA, fullText = "", ""
for s in open("24-s1.txt"):
  if not sMinA or s.count('A') < sMinA.count('A'):
     sMinA = s
  fullText += s

from string import ascii_uppercase

mostFreq = None
for c in ascii_uppercase:
  freq = sMinA.count(c)
  if not mostFreq or freq >= mostFreq[1]:
    mostFreq = (c, freq)

print( mostFreq[0], fullText.count(mostFreq[0]) )

"""
ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("24-s1.txt") as F:
  data = F.readlines()
  minK = 10**10
  for s in data:
    k = s.count('A')
    if k < minK:
      minK = k
      ma, letterMax = 0, ''
      for letter in ABC:
        cnt = s.count(letter)
        if cnt >= ma:
          ma, letterMax = cnt, letter

print( letterMax,
       sum(s.count(letterMax) for s in data) )
"""
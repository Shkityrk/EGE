with open("24-168.txt") as F:
  s = F.readline()

#s = 'AABBAABBCCDDDEFFGF'

letters = s[0]
counts = [1]
for i in range(1,len(s)):
  if s[i] == s[i-1]:
    counts[-1] += 1
  else:
    letters += s[i]
    counts.append( 1 )

#print( letters, counts )

Lmax = 0
for i in range(2,len(letters)):
  if letters[i-2] < letters[i-1] < letters[i]:
    L = sum(counts[i-2:i+1])
    Lmax = max( L, Lmax )

print( Lmax )
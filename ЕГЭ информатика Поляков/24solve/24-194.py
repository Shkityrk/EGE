with open('24-191.txt') as F:
  s = F.readline()

WAIT_A = 0
WAIT_B = 1
chunks = []
state = WAIT_A
for i, c in enumerate(s):
  if state == WAIT_A:
    if c == 'A':
      state = WAIT_B
      ch = ''
  elif state == WAIT_B:
    if c == 'B':
      if len(ch) <= 13 and 'F' in ch:
        chunks.append( ch )
      state = WAIT_A
      ch = ''
    elif c == 'A':
      ch = ''
    else:
      ch += c

print( len(chunks) )
#print( chunks )


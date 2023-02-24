s=open('K/24-25.txt').readline()
sub='DBAC'
while sub in s:
    sub+='DBAC'
while sub not in s:sub=sub[:-1]
print(len(sub))
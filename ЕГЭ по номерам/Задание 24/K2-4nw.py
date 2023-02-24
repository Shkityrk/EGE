s=open('K2/24-4.txt').readline()
s=s.replace('JBOSS',' ').replace('BOSSJ',' ')
print(s.count('BOSS'))
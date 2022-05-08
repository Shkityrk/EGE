import string

alphabet = list(string.ascii_uppercase)

with open("s2.txt") as file:
    s = file.readline()

arr = []
for i in alphabet:
    x = s.count('X' + i + 'Y')
    arr.append((x, i))

print(max(arr, key=lambda x: x[0]))
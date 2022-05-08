// Автор В.Н. Шубинкин
##
assign(input, '24-j9.txt');
var s := Readlnstring;
var k := 0;
for var i := 1 to s.Length - 4 do
  if s[i:i + 5] = s[i:i + 5][::-1] then
    k += 1;
print(k); 
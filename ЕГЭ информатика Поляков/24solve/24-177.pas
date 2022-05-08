// Автор В.Н. Шубинкин
##
assign(input, '24-157.txt');
var s := Readlnstring;
var k := 1;  // k - позиция начала текущей подходящей цепочки символов
var maxLen := 0;
for var i := 2 to s.Length do
begin
  if (s[i - 1] + s[i] = 'PR') or (s[i - 1] + s[i] = 'RP') then
  begin
    if i - k > maxLen then 
      maxLen := i - k;
    k := i;
  end;  
end;
print(maxLen); 
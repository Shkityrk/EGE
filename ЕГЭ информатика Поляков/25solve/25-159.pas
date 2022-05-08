// Автор: С.П. Пуляшкина
##
uses school;
var a:=700001;
var k:=0;
while k <4 do begin 
  if a.Divisors.Count < (a+1).Divisors.Count
  then k+=1 else k:=0;
  a+=1;
end;
for var z:=a-4 to a do
  Println( z, z.Divisors.Count )
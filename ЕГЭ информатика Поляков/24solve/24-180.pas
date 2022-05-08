// Автор: А. Богданов
##
Assign(input, '24-180.txt');
var a := ReadString;

var k := |0|*4;
var kMax := 0;
for var i:=1 to a.Length-3 do begin
  var (h10, h1, m10, m1) := a[i:i+4].Select(x->x.ToDigit);
  if (h10*10+h1 < 24)and(m10*10+m1 < 60) then begin
    k[i mod 4] += 1;
    kMax := max(kMax, k[i mod 4]);
  end else
    k[i mod 4] := 0;
end;

Print( kMax )

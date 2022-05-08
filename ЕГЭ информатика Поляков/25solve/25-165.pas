// Автор: С.П. Пуляшкина
##
var m := 0;
while m < 30 do begin
  var n := 1;
  while n<11 do begin
    var x:= Power(2,m)*Power(7,n);
    if (x>=100000000) and (x<=300000000) then 
      writeln( x, '  ', m+n );
    n := n+2;
  end;
  m:=m+2;
end;

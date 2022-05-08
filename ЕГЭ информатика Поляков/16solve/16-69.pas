// Автор: Зубов Н.С.
function F( n: integer ): integer;
begin
  if n < 4  then 
    Result := n-1;
    if (n > 3) and (n mod 3=0)  then 
  Result :=n+ 2*F(n-1)
  else
    Result :=F(n-2)+F(n-3)
end;
begin
  writeln( F(25) );
end.

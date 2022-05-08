var s: string; 
    count, i:integer; 
begin 
  assign( input, '24-j5.txt' ); 
  readln(s); 
  count := 0; 
  for i:=3 to length(s)-2 do 
    if (s[i] = 'O') AND (s[i+1] = 'C') AND (s[i+2] = 'K') AND
       ((s[i-1] <> 'T') OR (s[i-2] <> 'S')) then begin
       count := count + 1;
    end;
  writeln( count ); 
end.

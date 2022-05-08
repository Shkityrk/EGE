var F: text;
    s: string;
    p, count: integer;
begin 
  assign( F, '24-s1.txt' ); 
  reset( F );
  count := 0;
  while not eof( F ) do begin 
    readln( F, s ); 
    p := Pos( 'YZ', s );
    if  p > 0 then
      if Pos( 'YZ', Copy(s,p+2,Length(s)) ) > 0 then
        count := count + 1;
  end; 
  close( F );
  write( count );
end.
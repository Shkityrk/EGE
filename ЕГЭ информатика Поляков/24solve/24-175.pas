##
var s := ReadLines('24-175.txt').First.Replace('KEGE', '#');
var maxLen := 0;
var chunks := s.Split('#');
var allLen := chunks.Select( chunk-> Length(chunk) ).ToArray;
var N := allLen.Length;
for var i:=0 to N-3 do begin
  var L := allLen[i:i+3].Sum + 4*Length('KEGE') -2;
  if (i = 0) and (allLen[i] <> 0) then
    L -= Length('KEGE') - 1;  
  if (i = N-1) and (allLen[i] <> 0) then
    L -= Length('KEGE') - 1;  
  maxLen := max( L, maxLen );
end;  
Print( maxLen );

{
var s := ReadLines('24-175.txt').First;
var (stopPoints, maxlen) := (|0, 0, 0|, 0);
for var i:=4 to Length(s) do begin
  if s[i-3:i+1] = 'KEGE' then 
    stopPoints := stopPoints + |i-2|;
  maxLen := max( i - stopPoints[^3] + 1,
                 maxLen );
end;  
Print( maxLen );
}

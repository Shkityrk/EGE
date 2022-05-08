##
var s := ReadLines('24-181.txt').First;
var K := 3;   // сколько гласных разрешается
var stopPoints := |-1|;
var maxLen := 0;
for var i:=1 to Length(s) do begin
  if s[i] = '.' then
    stopPoints := |i|;
  if s[i] in 'AEIOUY' then begin
    if Length(stopPoints) > K then
      stopPoints := stopPoints[1:];
    stopPoints := stopPoints + |i|;
  end;
  maxLen := max( i - stopPoints[0], maxLen );
end;
Print( maxLen );

{
var s := ReadLines('24-181.txt').First;
var K := 7;   // сколько гласных разрешается
var stopPoints := |-1|*(K+1);
var maxLen := 0;
for var i:=1 to Length(s) do begin
  if s[i] = '.' then
    stopPoints := |i|*(K+1);
  if s[i] in 'AEIOUY' then
    stopPoints := |i| + stopPoints;
  maxLen := max( i - stopPoints[K], maxLen );
end;
Print( maxLen );
}
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

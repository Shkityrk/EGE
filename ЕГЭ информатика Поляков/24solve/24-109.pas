// Автор: В.Н. Шубинкин

begin
  assign(input, '24-1.txt');
  var s: string;
  read(s);
  var k := 1;
  var maxim := 0;
  for var i := 2 to length(s) do
    if s[i] < s[i - 1] then
    begin
      k += 1;
      if k > maxim then maxim := k
    end
    else k := 1;
    write(maxim)
end.
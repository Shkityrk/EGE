// Автор: В.Н. Шубинкин

begin  
  //var s := ReadAllText('24-4.txt'); - опасно использовать,
  //так как в s окажутся в том числе непечатные символы
  //и ответ для убывающей подпоследовательности может быть неверным,
  //если таковая в конце
  assign(input, '24-4.txt');
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
    writeln(maxim)
end.
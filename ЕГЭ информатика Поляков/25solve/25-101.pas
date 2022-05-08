// Автор: С.П. Пуляшкина
##
uses school;
var z:=(125697..190234).Where(
        x -> (x.Factorize.Distinct.Count=2) 
             and (x.Divisors.Count = 4)); 
Println( z.Count, z.Max );


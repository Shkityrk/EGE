##
var allLines := ReadAllLines('24-s1.txt');
var sMinA := allLines.minBy( s -> s.CountOf('A') );
var letCount := 
   ('A'..'Z').Select( c-> (c, sMinA.CountOf(c)) );
var maxCount := letCount.MaxBy( \(c,count)->count )[1];   
var letter := letCount
  .Where( \(c,count)-> count = maxCount )
  .Select( \(c,count)-> c ).Last;
var count := allLines.Select( s->s.CountOf(letter) ).Sum;   
Print( letter, count );




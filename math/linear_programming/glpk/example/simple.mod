# by the way, the space in the equations is just to make it look neat

var x1;
var x2;
var x3;
maximize obj: x1 + 2 * x2 + 3 * x3;
s.t. c1: x1 <= 1;
s.t. c2: x2 <= 2;
s.t. c3: x3 <= 3;
solve;
display x1, x2, x3;
end;

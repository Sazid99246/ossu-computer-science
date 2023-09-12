fun double x = x * 2;
fun incr x = x + 1;
val a_tuple = (double, incr, double(incr 7));
val eighteen = (#1 a_tuple) 9;

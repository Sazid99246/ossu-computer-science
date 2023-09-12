fun n_times (f,n,x) = 
    if n=0
    then x
    else f (n_times(f,n-1,x))


fun triple_n_times1 (n,x) =
    n_times ((fn x => 3*x, n, x));

datatype mytype = TwoInts of int * int 
                | Str of string 
                | Pizza

(* mytype -> int *)
fun f (x : mytype) = 
    case x of 
	Pizza => 3 
      | Str s => 8
      | TwoInts(i1,i2) => i1 + i2

(*    | Pizza => 4; (* redundant case: error *) *)
(*fun g x = case x of Pizza => 3 (* missing cases: warning *) *)

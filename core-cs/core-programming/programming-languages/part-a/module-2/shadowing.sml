val a = 20;

(* a : int
   a -> 10 *)

val b = a * 2;

(* a -> 10
   b -> 20  *)

val a = 5;

(* b -> 20 *)

val c = b;

(* a -> 5, b -> 20, c -> 20*)

val d = a;

(*.... d -> 5 *)

a = a + 1;
(*..., a -> 6 *)

(* val g = f - 3 *)

val f = a * 2;

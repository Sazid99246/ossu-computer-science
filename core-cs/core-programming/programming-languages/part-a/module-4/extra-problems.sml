(* Compose two functions with 'option' values *)
fun compose_opt f g x =
    case g x of
        NONE => NONE
      | SOME y => f y;

(* Apply function 'f' repeatedly to 'x' until 'p' returns false *)
fun do_until f p x =
    if p x then
        do_until f p (f x)
    else
        x;

(* Implement factorial using do_until *)
fun factorial n =
    let
        val is_zero = fn x => x = 0
        val decrement = fn x => x - 1
        val multiply = fn x => x * n
    in
        do_until decrement is_zero 1
    end;

(* Find the fixed point of a function 'f' *)
fun fixed_point f x =
    if f x = x then
        x
    else
        fixed_point f (f x);
		    
(* Map a function 'f' over a pair of values *)
fun map2 f (x, y) =
    (f x, f y)

(* Apply 'f' to every element of the list 'g x' and concatenate the results *)
fun app_all f g x =
    List.concat (List.map f (g x));

(* Implement List.foldr *)
fun foldr f a xs =
    case xs of
        [] => a
      | x::rest => f (x, foldr f a rest);

(* Partition a list into two lists based on a predicate *)
fun partition p xs =
    let
        fun partition' (yes, no) [] = (yes, no)
          | partition' (yes, no) (x::rest) =
            if p x then
                partition' (x::yes, no) rest
            else
                partition' (yes, x::no) rest
    in
        partition' ([], []) xs
    end;

(* Unfold a function to generate a list *)
fun unfold f seed =
    case f seed of
        NONE => []
      | SOME (x, new_seed) => x :: unfold f new_seed;

(* Implement factorial using unfold and foldl *)
fun factorial' n =
    let
        val is_zero = fn x => x = 0
        val decrement = fn x => x - 1
        val multiply = fn (x, acc) => (x * acc, decrement x)
    in
        foldl multiply 1 (unfold (fn n => if n = 0 then NONE else SOME(n, n-1)) n)
    end;

(* Implement map using List.foldr *)
fun map f xs =
    foldr (fn (x, acc) => f x :: acc) [] xs;

(* Implement filter using List.foldr *)
fun filter p xs =
    foldr (fn (x, acc) => if p x then x :: acc else acc) [] xs;

(* Implement foldl using foldr *)
fun foldl f a xs =
    foldr (fn (x, acc) => fn y => f (x, y)) (fn x => x) xs a;

(* Define a binary tree type and map and fold functions *)
datatype 'a Tree = Leaf | Node of 'a * 'a Tree * 'a Tree;

fun map_tree f tree =
    case tree of
        Leaf => Leaf
      | Node (data, left, right) => Node (f data, map_tree f left, map_tree f right);

fun fold_tree f acc tree =
    case tree of
        Leaf => acc
      | Node (data, left, right) =>
        let
            val acc' = f data (fold_tree f acc left)
        in
            fold_tree f acc' right
        end;

(* Define filter_tree where "false" means replacing the subtree with a leaf *)
fun filter_tree p tree =
    case tree of
        Leaf => Leaf
      | Node (data, left, right) =>
        if p data then
            Node (data, filter_tree p left, filter_tree p right)
        else
            Leaf;

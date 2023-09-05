type student_id = int;
type grade = int (* must be in 0 to 100 range *)
type final_grade = { id : student_id, grade : grade option };
datatype pass_fail = pass | fail;

fun pass_of_fail {grade = SOME g, id} =
    if g >= 75
    then pass
    else fail
  | pass_of_fail {grade=NONE, id} = fail;

fun has_passed {grade = SOME g, id} = g >= 75
  | has_passed {grade = NONE, id} = false;

fun number_passed grades =
    List.filter (fn x => has_passed x) grades |> length;

fun number_misgraded grades =
    List.filter (fn (pf, fg) => if pf = pass then not (has_passed fg) else has_passed fg) grades |> length;

datatype 'a tree = leaf 
                 | node of { value : 'a, left : 'a tree, right : 'a tree }
datatype flag = leave_me_alone | prune_me;

fun tree_height leaf = 0
  | tree_height (node {left, right, ...}) =
    1 + Int.max (tree_height left) (tree_height right);

fun tree_height leaf = 0
  | tree_height (node {left, right, ...}) =
    1 + Int.max (tree_height left) (tree_height right);

fun gardener leave_me_alone = leave_me_alone
  | gardener (prune_me) = leaf
  | gardener (node {value, left, right}) =
    node {value = value, left = gardener left, right = gardener right};

fun last [] = NONE
  | last [x] = SOME x
  | last (_::xs) = last xs;

fun take (0, _) = []
  | take (_, []) = []
  | take (n, x::xs) = x :: take (n - 1, xs);

fun drop (0, xs) = xs
  | drop (_, []) = []
  | drop (n, _::xs) = drop (n - 1, xs);

fun concat [] = []
  | concat (x::xs) = x @ concat xs;

fun getOpt (x, SOME y) = y
  | getOpt (x, NONE) = x;

fun join (sep, []) = ""
  | join (sep, [x]) = x
  | join (sep, x::xs) = x ^ sep ^ join (sep, xs);

fun is_positive ZERO = false
  | is_positive (SUCC _) = true;

exception Negative

fun pred ZERO = raise Negative
  | pred (SUCC n) = n;

fun nat_to_int ZERO = 0
  | nat_to_int (SUCC n) = 1 + nat_to_int n;

fun int_to_nat n =
    if n < 0 then raise Negative
    else if n = 0 then ZERO
    else SUCC (int_to_nat (n - 1));

fun add (x, ZERO) = x
  | add (x, SUCC y) = SUCC (add (x, y));

fun sub (x, ZERO) = x
  | sub (SUCC x, SUCC y) = sub (x, y)
  | sub (_, ZERO) = raise Negative
  | sub (ZERO, _) = ZERO;

fun mult (_, ZERO) = ZERO
  | mult (x, SUCC y) = add (x, mult (x, y));

fun less_than (ZERO, _) = true
  | less_than (_, ZERO) = false
  | less_than (SUCC x, SUCC y) = less_than (x, y);

fun isEmpty (Elems xs) = null xs
  | isEmpty _ = false

17. `contains` function:
```sml
fun contains (Elems xs, n) = List.exists (fn x => x = n) xs
  | contains (Range {from, to}, n) = n >= from andalso n <= to
  | contains (Union (s1, s2), n) = contains (s1, n) orelse contains (s2, n)
  | contains (Intersection (s1, s2), n) = contains (s1, n) andalso contains (s2, n);

fun toList (Elems xs) = List.sort (fn (x, y) => x < y) (List.duplicates xs)
  | toList (Range {from, to}) = List.tabulate (to - from + 1, fn i => from + i)
  | toList (Union (s1, s2)) = List.duplicates (toList s1 @ toList s2)
  | toList (Intersection (s1, s2)) = List.filter (fn x => contains (s1, x) andalso contains (s2, x)) (toList s1);

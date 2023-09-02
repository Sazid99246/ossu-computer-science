fun alternate (loi : int list) =
    if null loi
    then 0
    else if length loi = 1 then hd loi
    else hd loi - hd (tl loi) + alternate (tl (tl loi));

fun min_max (loi : int list) =
    let
        fun min_max_helper (lst, min, max) =
            case lst of
                [] => (min, max)
              | hd::tl => if hd < min then min_max_helper(tl, hd, max)
                          else if hd > max then min_max_helper(tl, min, hd)
                          else min_max_helper(tl, min, max)
    in
        if null loi
        then NONE
        else let
            val (min, max) = min_max_helper (loi, hd loi, hd loi)
        in
            SOME (min, max)
        end
    end;

fun cumsum_helper [] _ acc = List.rev acc
  | cumsum_helper (x::xs) sumSoFar acc =
    let
      val currentSum = sumSoFar + x
    in
      cumsum_helper xs currentSum (currentSum::acc)
    end;

fun cumsum xs = cumsum_helper xs 0 [];

fun greeting (s : string option) =
    case s of
	SOME name => "Hello there, " ^ name ^ "!"
      | NONE => "Hello there, you";

fun repeat ([], []) = []
  | repeat(_, []) = []
  | repeat([], _) = []
  | repeat(x::xs, n::ns) =
    if n < 0 then
      raise Fail "Negative count in the second list."
    else
	List.tabulate(n, fn _ => x) @ repeat(xs, ns);

fun addOpt (x : int option, y : int option) =
    case (x, y) of
	(SOME a, SOME b) => SOME (a + b)
      | _ => NONE;

fun addAllOpt (lst: int option list) =
    let
        fun sumSomeValues([], acc) = acc
          | sumSomeValues(SOME x :: rest, acc) = sumSomeValues(rest, acc + x)
          | sumSomeValues(NONE :: rest, acc) = sumSomeValues(rest, acc)
    in
        case sumSomeValues(lst, 0) of
            0 => NONE
          | sum => SOME sum
    end;

fun any (lob : bool list) =
    if null lob
    then false
    else if (hd lob) = true
    then true
    else any (tl lob);			   
	     
fun all (lob : bool list) =
    case lob of
	[] => true
      | true::rest => all(rest)
      | false::_ => false;

fun zip ([], _) = []
  | zip(_, []) = []
  | zip(x::xs, y::ys) = (x, y) :: zip(xs, ys);

fun zipRecycle ([], _) = []
  | zipRecycle(_, []) = []
  | zipRecycle(xs, ys) = 
      let
          fun zipRecycleHelper([], _, origXs, ys, acc) =
              zipRecycle(origXs, ys) @ rev acc  (* Recycle xs from the beginning *)
            | zipRecycleHelper(_, [], xs, origYs, acc) =
              zipRecycle(xs, origYs) @ rev acc  (* Recycle ys from the beginning *)
            | zipRecycleHelper(x::xs, y::ys, origXs, origYs, acc) =
              zipRecycleHelper(xs, ys, origXs, origYs, (x, y) :: acc)
      in
          zipRecycleHelper(xs, ys, xs, ys, [])
      end;

fun zipOpt (xs: int list, ys: int list) =
    let
        fun zipHelper([], []) = SOME []
          | zipHelper(x::xs, y::ys) =
            (case zipHelper(xs, ys) of
                NONE => NONE
              | SOME rest => SOME ((x, y)::rest))
          | zipHelper(_, _) = NONE  (* Catch-all pattern for unequal list lengths *)
        val xsLength = length xs
        val ysLength = length ys
    in
        if xsLength = ysLength then zipHelper(xs, ys) else NONE
    end;

fun lookup (lst: (string * int) list, s2: string) =
    case List.find (fn (s, i) => s = s2) lst of
        SOME (_, i) => SOME i
      | NONE => NONE;

fun splitup (lst: int list) =
    let
        fun split([], pos, neg) = (rev pos, rev neg)
          | split(x::xs, pos, neg) =
            if x >= 0 then split(xs, x::pos, neg)
            else split(xs, pos, x::neg)
    in
        split(lst, [], [])
    end;

fun splitAt (lst: int list, threshold: int) =
    let
        fun split([], pos, neg) = (rev pos, rev neg)
          | split(x::xs, pos, neg) =
            if x >= threshold then split(xs, x::pos, neg)
            else split(xs, pos, x::neg)
    in
        split(lst, [], [])
    end;

fun isSorted (lst: int list) =
    let
        fun check([], _) = true
          | check(_, []) = true
          | check(x::xs, y::ys) =
            if x <= y then check(xs, ys)
            else false
    in
        check(lst, tl lst)
    end;

fun isAnySorted (lst: int list) =
    isSorted(lst) orelse isSorted(List.rev lst);

fun sortedMerge (lst1: int list, lst2: int list) =
    let
        fun merge([], ys) = ys
          | merge(xs, []) = xs
          | merge(x::xs, y::ys) =
            if x <= y then x :: merge(xs, y::ys)
            else y :: merge(x::xs, ys)
    in
        merge(lst1, lst2)
    end;

fun qsort ([]) = []
  | qsort(x::xs) =
    let
        val (smaller, larger) = splitAt(xs, x)
    in
        sortedMerge(qsort(smaller), x :: qsort(larger))
    end;

fun divide (lst: int list) =
    let
        fun divideHelper([], odds, evens) = (rev odds, rev evens)
          | divideHelper(x::xs, odds, evens) =
            if x mod 2 = 0 then divideHelper(xs, odds, x::evens)
            else divideHelper(xs, x::odds, evens)
    in
        divideHelper(lst, [], [])
    end;

fun not_so_quick_sort ([]) = []
  | not_so_quick_sort([x]) = [x]
  | not_so_quick_sort(lst) =
    let
        val (odds, evens) = divide(lst)
    in
        sortedMerge(not_so_quick_sort(odds), not_so_quick_sort(evens))
    end;

fun fullDivide (k: int, n: int) =
    let
        fun fullDivideHelper(k, n, d) =
            if k mod n = 0 then fullDivideHelper(k div n, n, d + 1)
            else (d, k)
    in
        fullDivideHelper(k, n, 0)
    end;

fun factorize (n: int) =
    let
        fun factorizeHelper(n, d) =
            if d * d > n then []
            else
                let
                    val (count, reducedN) = fullDivide(n, d)
                in
                    if count > 0 then (d, count) :: factorizeHelper(reducedN, d + 1)
                    else factorizeHelper(n, d + 1)
                end
    in
        factorizeHelper(n, 2)
    end;

fun multiply (factorization : (int * int) list) =
    let
        fun multiplyHelper([]) = 1
          | multiplyHelper((d, k)::rest) = d * k * multiplyHelper(rest)
    in
        multiplyHelper(factorization)
    end;

fun all_products (factorization: (int * int) list) =
    let
        fun generateProducts([], current, products) =
            rev (current :: products)
          | generateProducts((d, k)::rest, current, products) =
            let
                fun powersHelper(_, 0, powers) = powers
                  | powersHelper(base, exp, powers) =
                    powersHelper(base, exp - 1, base * exp :: powers)
                val powers = powersHelper(d, k, [])
                fun combine(x, y) = x * y
            in
                generateProducts(rest, ListPair.map combine (powers, current), products)
            end
    in
        generateProducts(factorization, [1], [])
    end;

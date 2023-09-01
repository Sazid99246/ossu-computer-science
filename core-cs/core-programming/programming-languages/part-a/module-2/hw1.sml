(* Task 1 *)
fun is_older (x : int*int*int, y : int*int*int) =
    if #1 x < #1 y
    then true
    else if #1 x > #1 y
    then false
    else if #2 x < #2 y
    then true
    else if #2 x > #2 y
    then false
    else if #3 x < #3 y
    then true
    else false;

(* Task 2 *)
fun number_in_month (lod : (int * int * int) list, month: int) =
    if null lod
    then 0
    else if ((#2 (hd lod)) = month)
    then 1 + number_in_month(tl lod, month)
    else number_in_month(tl lod, month);

(* Task 3 *)
fun number_in_months (lod : (int * int * int) list, lom : int list) =
    (* here lod means "list of date" and lom means "list of month" *)
    if null lom
    then 0
    else number_in_month(lod, (hd lom)) + number_in_months(lod, (tl lom));

(* Task 4 *)
fun dates_in_month (lod : (int * int * int) list, month : int) =
    if null lod
    then []
    else if ((#2 (hd lod)) = month)
    then (hd lod) :: dates_in_month(tl lod, month)
    else dates_in_month(tl lod, month);

(* Task 5 *)
fun dates_in_months (lod : (int * int * int) list, lom : int list) =
    if null lom
    then []
    else dates_in_month(lod, (hd lom)) @ dates_in_months(lod, (tl lom));

(* Task 6 *)
fun get_nth (los : string list, n : int) =
    if n = 1
    then hd los
    else get_nth(tl los, n - 1);

(* Task 7 *)
fun date_to_string (date : int * int * int) =
    let val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	val month = get_nth(months, #2 date);
    in month ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
    end;

(* Taask 8 *)
fun number_before_reaching_sum(sum : int, nums: int list) =
  let fun number_before_reaching_sum_helper(nums : int list, target : int, total : int, n : int) =
	if total + (hd nums) < target 
	then number_before_reaching_sum_helper(tl nums, target, total + (hd nums), n + 1)
	else n
  in number_before_reaching_sum_helper(nums, sum, 0, 0)
  end;

(* Task 9 *)
fun what_month(day : int) =
  let val month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  in number_before_reaching_sum(day, month_lengths) + 1
  end;
      
(* Task 10 *)
fun month_range(day1 : int, day2 : int) =
  if day1 > day2
  then []
  else what_month(day1) :: month_range(day1 + 1, day2);

(* Task 11 *)
fun oldest(dates : (int * int * int) list) =
  if null dates
  then NONE
  else let
      fun oldest_nonempty(dates : (int * int * int) list) =
	if null (tl dates)
	then hd dates
	else let val tl_ans = oldest_nonempty(tl dates)			     
	     in
		 if is_older(hd dates, tl_ans)	    
		 then hd dates
		 else tl_ans
	     end
  in
      SOME (oldest_nonempty dates)	   
  end;

(* Task 13 *)
fun reasonable_date(date) =
    let
        val (year, month, day) = date
        val validMonth = month >= 1 andalso month <= 12

        fun is_leap_year(year) =
            (year mod 400 = 0) orelse ((year mod 4 = 0) andalso (year mod 100 <> 0));

        val validDay = case month of
                            2 => day >= 1 andalso day <= (if is_leap_year(year) then 29 else 28)
                          | 4 | 6 | 9 | 11 => day >= 1 andalso day <= 30
                          | _ => day >= 1 andalso day <= 31
    in
        year > 0 andalso validMonth andalso validDay
    end;


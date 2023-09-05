(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2;

(* put your solutions for problem 1 here *)
fun all_except_option (s, xs) = 
    case xs of
	[] => NONE
      | x::xs' => if same_string(x, s)
		  then SOME xs'
		  else case all_except_option(s, xs') of
			   NONE => NONE 
			 | SOME tail => SOME (x::tail);

fun get_substitutions1 (list, s) =
  case list of
      [] => []
    | l::list' => case all_except_option(s, l) of
		    NONE => [] 
		   | SOME sublist => sublist @ get_substitutions1(list', s);

fun get_substitutions2 (list, s) =
  let
      fun extract_list_val(opt) =
	case opt of
	    NONE => []
	  | SOME sublist => sublist
      fun get_sub_helper(list, s, acc) =
	case list of
	    [] => acc
	  | l::list'=> get_sub_helper(list', s, acc @ extract_list_val(all_except_option(s, l)))
  in
      get_sub_helper(list, s, [])
  end;

fun similar_names (list, name) =
  let fun similar_helper(subs, name) =
	case subs of
	    [] => []
	  | sub::subs' => case name of
			      {first=x, last=y, middle=z} =>
			      [{first=sub, last=y, middle=z}] @ similar_helper(subs', name)
  in
      case name of
	  {first=x, middle=y, last=z} =>
	  let
	      val firstname_subs = get_substitutions2(list, x)
	  in
	      name::similar_helper(firstname_subs, name)
	  end
  end;



(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades;
datatype rank = Jack | Queen | King | Ace | Num of int; 
type card = suit * rank;

datatype color = Red | Black;
datatype move = Discard of card | Draw; 

exception IllegalMove;

(* put your solutions for problem 2 here *)
fun card_color (card) =
    case card of
	(Clubs, _) => Black
      | (Spades, _) => Black
      | (_, _) => Red;

fun card_value (card) =
    case card of
	(_, Ace) => 11
      | (_, Num n) => n
      | (_, _) => 10;

fun remove_card ([], c: card, e) = raise e
  | remove_card (x :: cs, c, e) =
    case x=c of
	true => cs
     |  false  => x :: remove_card (cs, c, e);

fun all_same_color ([]) = true
  | all_same_color (c::cs) = 
	let val starter = card_color(c)
		fun helper ([]) = true
		| helper (x :: xs) =
		case card_color(x) = starter of
			false => false
		      | true => helper(xs)
	in helper (cs)
	end;

fun sum_cards (cs: card list) =
    let fun helper (cs, acc) =
	    case cs of
		[] => acc
	      | c :: cs' => helper (cs', card_value(c) + acc)
    in
	helper (cs, 0)
    end;

fun score ([], goal: int) = goal
  | score (cs: card list, goal: int) = 
    let val sum = sum_cards(cs)
        val prelim = case sum <= goal of
			 true => goal - sum
		      | false => 3*(sum - goal)
    in case all_same_color(cs) of
	   false => prelim
	 | true  => prelim div 2
    end;
	
fun officiate (cl: card list, ml: move list, goal: int) =
    let fun helper (hl, [], ml, goal) = score(hl, goal)
	  | helper (hl, cl, [], goal) = score(hl, goal) 
	  | helper (hl: card list, cl, ml, goal) =
	    case sum_cards(hl) > goal of
		true => score(hl, goal)
	      | false => case ml of
			     [] => score (hl, goal)
			   | m :: ms => case m of
					    Discard cd => helper(remove_card(hl, cd, IllegalMove), cl, ms, goal)
					  | Draw => case cl of
							[] => score(hl, goal)
						      | c :: cs =>  helper(c :: hl, remove_card(cl, c, IllegalMove), ms, goal)
    in helper([], cl, ml, goal)
    end

fun check_num_aces (cardlist, acc) =
    let fun check_number_of_aces ([], acc) = acc
	  | check_number_of_aces (c::cs, acc) = case c of
						    (_, Ace) => check_number_of_aces(cs, acc + 1)
						  | _  => check_number_of_aces(cs, acc)
    in check_number_of_aces (cardlist, 0)
    end;

fun lowest_score (cs, pcs, lowest, goal) =
    case cs of
	[] => lowest
      | (suit, Ace)::rest =>
	let val cst = pcs @ [(suit, Num 1)] @ rest
	    val curr_score = score(cst, goal)
	in
	    if curr_score < lowest
	    then lowest_score(rest, pcs @ [(suit, Num 1)], curr_score, goal)
	    else lowest_score(rest, pcs @ [(suit, Ace)], lowest, goal)
	end
      |  c::rest => lowest_score(rest, pcs @ [c], lowest, goal);

(* Score_challenge and officiate_challenge are not entirely mine, had to look up stuff*)

fun score_challenge (cs, goal) =
    let val regular_score = score(cs, goal)
    in lowest_score(cs, [], regular_score, goal)
    end;

fun officiate_challenge (cs, ml, goal) =
    let fun play_moves(cs, hl, ml) =
	    case ml of
		[] => hl
	      | Discard c::ms => play_moves(cs, remove_card(hl, c, IllegalMove), ms)
	      | Draw::ms => case cs of
				[] => hl
			      | c::rest =>
				if (card_value(c) + sum_cards(hl)) > goal
				then c::hl
				else play_moves(rest, c::hl, ms)
    in
	score_challenge(play_moves(cs, [], ml), goal)
    end;
	
				      
fun discard_check (hl, c, goal) = 
    let val diff = goal - sum_cards(c::hl)
	fun check_if_val([], diff) = NONE
	  | check_if_val (h::hl, diff) = case card_value(h) = diff of
					     false => check_if_val(hl, diff)
					   | true => SOME h
    in check_if_val(hl, diff)
    end;
	
fun careful_player (cl, goal) =
    let fun helper (ml, hl, [], goal) = ml
	  | helper (ml, hl, c::cs, goal) =
	    case score(hl, goal) of 
		0 => ml
	      | _ => case discard_check(hl, c, goal) of
			 NONE => helper(Draw::ml, c::hl, cs, goal)
		       | SOME x => helper((Draw::(Discard x::ml)), c::remove_card(hl, x, IllegalMove), cs, goal)
    in helper([],[],cl,goal)
    end;

<?php
$input = file('/home/doomnonius/advent-of-code/2025/day02.input');

$t = 0;

foreach (explode(",", trim($input[0])) as $r) {
	echo "range is $r<br>";
	$r = explode("-", $r);
	$lo = $r[0];
	$hi = $r[1];
	$l = strlen($lo);
	$l2 = strlen($hi);
	if ($l != $l2) echo "mismatch!<br>";
	if ($l % 2 > 0 && $l == $l2) echo "no bad ids in range $lo-$hi<br>";
	else {
		if ($l % 2 > 0) {
			# find lowest even digited number in range
			$a = 10 ** (($l-1)/2);
		}
		else $a = intdiv(intval($lo), 10 ** ($l/2));
		$breaker = false;
		while (!$breaker) { # ($a <= intdiv(intval($hi), (10 ** ($l2/2)))) {
			$c = intval(strval($a).strval($a));
			if ($c >= $lo && $c <= $hi) {
				$t += $c;
				/* if ($t < 1227775554) echo "added $c, new total: $t<br>"; */
				$a += 1;
			}
			elseif ($c > $hi) $breaker = true;
			elseif ($c < $lo) $a += 1;
		}
	}
	echo "end<br>";
}

$t2 = 0;
# TODO: When odd, the only possible patterns are 1char repeating for full length, 3char repeating in 9, so 5, 7, 11 only possible is all same
# evens has all same, 2char repeating 2+X, 3char repeating 2-3X, 4char 2X, 5char 2X
# can we easily build all possibles in the range for each potential line?


echo "$t<br>"; # 9310318126 is too low, as is 14859665791, 18595663903
?>

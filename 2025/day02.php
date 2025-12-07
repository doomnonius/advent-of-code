<?php
$input = file('/home/doomnonius/advent-of-code/2025/day02.input');

$bad1 = [];
$bads = [];

foreach (explode(",", trim($input[0])) as $r) {
	echo "range is $r<br>";
	$r = explode("-", $r);
	$lo = $r[0];
	$hi = $r[1];
	$l = strlen($lo);
	$l2 = strlen($hi);
	if ($l != $l2) echo "mismatch!<br>";
	if ($l % 2 > 0 && $l == $l2) {
		echo "no bad ids in range $lo-$hi for p1<br>";
	}
	# TODO: I'm not accounting for when I have a even digit number first and then an odd digit number
	# idea: check if $l is even and $l2 is odd, and then start from 10 ** $l2-1 - ie do the second half first
	if ($l % 2 > 0 || ($l % 2 == 0 && $l2 % 2 > 0)) {
		# figure out which odd it is and therefore which patterns to check for
		# all odds have 1 digit repeating
		$bads = find_bad($lo, $hi, $l, intdiv($lo, 10 ** ($l-1)), $bads);
		# 9 is only one that can also have 3*3
		if ($l == 9) {
			$bads = find_bad($lo, $hi, 3, intdiv($lo, 10 ** 6), $bads);
		}
		# then: find lowest even digited number in range for when $lo is odd-digit and $hi is even digit
		if ($l2 % 2 == 0) $a = 10 ** $l;
		else continue;
	}
	else $a = $lo; # intdiv(intval($lo), 10 ** ($l-1));
	# TODO: check for each of 2, 3, 4, 5, 6(?)
	foreach ([2, 3, 4, 5, 6] as $f) {
		if ($l % $f ==  0) {
			$bads = find_bad($lo, $hi, $f, intdiv($a, 10 ** ()), $bads);
			if ($f == 2) $t = find_bad($lo, $hi, $f, intval(substr(strval($a), 0, $f)), $bads);
		}
	}
	echo "end<br>";
}

private function find_bad ($lo, $hi, $repeats, $a, $bad) {
	# break out this check into a function
	$breaker = false;
	while (!breaker) {
		$c = strval($a)
		$l = $repeats;
		while ($l > 1) {
			$c .= strval($a);
			$l -= 1;
		}
		if ($c >= $lo && $c <= $hi) {
			if (!in_aray($c, $bad)) $bad[] = $c;
			$a += 1;
		}
		elseif ($c > $hi) $breaker = false;
		elseif ($c < $lo) $a += 1;
	}
	return $bad;
}

# TODO: When odd, the only possible patterns are 1char repeating for full length, 3char repeating in 9, so 5, 7, 11 only possible is all same
# evens has all same, 2char repeating 2+X, 3char repeating 2-3X, 4char 2X, 5char 2X
# can we easily build all possibles in the range for each potential line?


echo sum($t)."<br>"; # 9310318126 is too low, as is 14859665791, 18595663903
echo sum($bads)."<br>";
?>

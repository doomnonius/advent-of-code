<?php
$input = file('/home/doomnonius/advent-of-code/2025/day02.input');

$bad1 = [];
$bads = [];

function find_bad ($lo, $hi, $repeats, $a, $bad) {
	$breaker = false;
	while (!$breaker) {
		$c = strval($a);
		$l = $repeats;
		while ($l > 1) {
			$c .= strval($a);
			$l -= 1;
		}
		$c = intval($c);
		if ($c >= $lo && $c <= $hi) {
			if (!in_array($c, $bad)) $bad[] = $c;
			$a += 1;
		}
		elseif ($c > $hi) $breaker = true;
		elseif ($c < $lo) $a += 1;
	}
	return $bad;
}

foreach (explode(",", trim($input[0])) as $r) {
	$r = explode("-", $r);
	$lo = $r[0];
	$hi = $r[1];
	$l = strlen($lo);
	$l2 = strlen($hi);
	# DONE check for each of 1, 2, 3, 4, 5, 6(?)
	foreach ([1, 2, 3, 4, 5, 6] as $f) {
		if ($l % $f == 0 && $f < $l) {
			$bads = find_bad(intval($lo), intval($hi), $l/$f, intdiv($lo, 10 ** ($l-$f)), $bads);
			if ($f == $l/2) $bad1 = find_bad(intval($lo), intval($hi), $l/$f, intdiv($lo, 10 ** ($l-$f)), $bad1);
		}
		if ($l != $l2 && $l2 % $f == 0 && $f < $l2) {
			$bads = find_bad(intval($lo), intval($hi), $l2/$f, 10**($f-1), $bads);
			if ($f == $l2/2) $bad1 = find_bad(intval($lo), intval($hi), $l2/$f, 10**($f-1), $bad1);
		}
	}
}

echo array_sum($bad1)."<br>"; # 9310318126 is too low, as is 14859665791, 18595663903
echo array_sum($bads)."<br>"; # first try!
?>

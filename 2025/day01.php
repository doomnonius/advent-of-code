<?php

$input = file('/home/doomnonius/advent-of-code/2025/day01.input');

$safe = 50;
$t = 0;
$t2 = 0;

foreach ($input as $y => $i) {
	$d = $i[0];
	$c = intval(substr($i, 1));
	$m = 10000;
	while ($c >= 100) {
		while ($c % $m == $c) $m /= 10;
		$t2 += (intdiv($c, $m) * ($m / 100));
		$c %= $m;
	}
	if ($c == 0) {
		if ($safe == 0) $t += 1;
		continue;
	}
	if ($d ==  "L") {
		if ($safe && $c >= $safe) $t2 += 1;
		$safe -= $c;
	}
	else {
		if ($c + $safe >= 100) $t2 += 1;
		$safe += $c;
	}
	if ($safe < 0) $safe = 100 - abs($safe);
	else $safe = $safe % 100;
	if ($safe == 0) {
		$t += 1;
	}
}

echo $t; # not 4196, too high
echo "<br>";
echo $t2; # not 5898, too low
?>

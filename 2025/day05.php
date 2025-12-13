<?php
$input = file('day05.input');

$t = 0;
$t2 = 0;

/* var_dump($input); */
$ranges = [];
$ids = [];
$r_flag = true;

foreach ($input as $i) {
	if ($r_flag && !str_contains($i, '-')) {
		$r_flag = false;
		continue;
	}
	if ($r_flag) {
		$ranges[] = array_map('intval', explode("-", $i));
		continue;
	}
	$ids[] = $i;
}

var_dump($ranges);
var_dump($ids[0]);

echo "$t<br>";
echo "$t2<br>";
?>

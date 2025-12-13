<?php
$input = file('/home/doomnonius/advent-of-code/2025/day03.input');

$t = 0;
$t2 = 0;

foreach ($input as $batts) {
	$batts = trim($batts);
	if (!$batts) continue;

	# first is largest int in 0:l-1
	$fir = max(str_split(substr($batts,0,-1)));
	# second is largest int in strpos(first):l
	$sec = max(str_split(substr($batts,strpos($batts,$fir)+1)));
	$t += intval("$fir$sec");
}

foreach ($input as $batts) {
	$batts = trim($batts);
	if (!$batts) continue;
	$count = 12;
	$val = '';
	while ($count > 0) {
		/* echo "batts: $batts<br>"; */
		/* echo "val: $val<br>"; */
		if ($count > 1) $val .= max(str_split(substr($batts,0,1-$count)));
		else $val .= max(str_split(substr($batts,0)));
		$batts = substr($batts, strpos($batts, substr($val,-1))+1);
		$count -= 1;
	}
	$t2 += intval($val);
}



echo "$t<br>";
echo "$t2<br>";
?>

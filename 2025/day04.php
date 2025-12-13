<?php
$all_coords = [];
$input = file('/home/doomnonius/advent-of-code/2025/day04.input');
foreach ($input as $y => $l) {
	$chars = str_split(trim($l));
	$all_coords[] = [];
	foreach ($chars as $x => $c) {
		$all_coords[$y][] = $c;
	}
}
$max_y = count($all_coords);
$max_x = count($all_coords[0]);
function get_octo ($x, $y, $max_x, $max_y) {
	if (($x + 1) > $max_x) {
		$tr = false;
		$r = false;
		$br = false;
	}
	if (($y + 1) > $max_y) {
		$bl = false;
		$b = false;
		$br = false;
	}
	if ($y === 0) {
		$tl = false;
		$t = false;
		$tr = false;
	}
	if ($x === 0) {
		$tl = false;
		$l = false;
		$bl = false;
	}
	if (!isset($tr)) $tr = [$x + 1, $y - 1];
	if (!isset($r)) $r = [$x + 1, $y + 0];
	if (!isset($br)) $br = [$x + 1, $y + 1];
	if (!isset($b)) $b = [$x + 0, $y + 1];
	if (!isset($bl)) $bl = [$x - 1, $y + 1];
	if (!isset($l)) $l = [$x - 1, $y + 0];
	if (!isset($tl)) $tl = [$x - 1, $y - 1];
	if (!isset($t)) $t = [$x + 0, $y - 1];
	$ret = [];
	foreach ([$tr, $r, $br, $b, $bl, $l, $tl, $t] as $c) {
		if ($c !== false) $ret[] = $c;
	}
	return $ret;
}

$t = 0;
$t2 = 0;
$loop = 0;

function remove_rolls($all_coords, $loop, $max_x, $max_y) {
	foreach ($all_coords as $y => $row) {
		foreach ($row as $x => $p) {
			if ($all_coords[$y][$x] != "@") continue;
			$nt = 0;
			$ns = get_octo($x, $y, $max_x, $max_y);
			foreach ($ns as $n) {
				if ($all_coords[$n[1]][$n[0]] == "@") $nt += 1;
			}
			if ($nt < 4) {
				$ret += 1;
				$to_remove[] = [$x, $y];
			}
		}
	}
	foreach ($to_remove as $rem) $all_coords[$rem[1]][$rem[0]] = '.';
	return [$all_coords, $loop, $ret];
}

while (true) {
	$a = remove_rolls($all_coords, $loop, $max_x, $max_y);
	if (!$a[2]) break;
	if (!$loop) $t += $a[2];
	$t2 += $a[2];
	$all_coords = $a[0]; # maybe unnecessary, depends on mutability of arrays in php
	$loop += 1;
}




echo "$t<br>"; # not 19461, too high; 
echo "$t2<br>";
?>

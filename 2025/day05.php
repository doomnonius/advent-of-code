<?php
$input = file('day05.input');

$t = 0;
$t2 = 0;

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
	$ids[] = intval($i);
}

foreach ($ids as $i) {
	foreach ($ranges as $r) {
		if ($i > $r[0] && $i < $r[1]) {
			$t += 1;
			break;
		}
	}
}

usort($ranges, function($a, $b) {
	return $a[0] <=> $b[0];
});

# compare ranges
# possible outcomes
# 1. range is exactly the same - will be dropped
# 2. range extends current range both directions
# 3. range extends current range lower
# 4. range extends current range higher
# 5. range fully contained in current range
# 6. both ends of range are equal to each other and an end of another range
# 7. range is different
function reduce_ranges($ranges) {
$updated_ranges = [$ranges[0]];
	foreach ($ranges as $r) {
		$to_add = null;
		foreach ($updated_ranges as $ind => $u) {
			if ($r[0] == $r[1]) $same = true; # used to find case 6
			else $same = false;
			if ($r[1] > $u[1] && $r[0] <= $u[1] + 1) { # case 4
				$updated_ranges[$ind][1] = $r[1];
				if ($r[0] < $u[0]) $updated_ranges[$ind][0] = $r[0]; # case 2
				$to_add = false;
			}
			elseif ($r[0] < $u[0] && $r[1] >= $u[0] - 1) { # case 3
				$updated_ranges[$ind][0] = $r[0];
				if ($r[1] > $u[1]) $updated_ranges[$ind][1] = $r[1]; # case 2 - shouldn't ever hit this though
				$to_add = false;
			}
			elseif (($r[0] == $u[0] && ($r[1] == $u[1] || $same)) || ($r[1] == $u[1] && $same)) { # case 6 and case 1
				$to_add = false;
			}
			elseif ($r[0] >= $u[0] && $r[1] <= $u[1]) { # case 5
				$to_add = false;
			}
			else {
				if ($to_add === null) $to_add = true; # case 7
			}
		}
		if ($to_add) $updated_ranges[] = $r;
	}
	return [$updated_ranges, count($ranges) == count($updated_ranges)];
}
$ret = reduce_ranges($ranges);
foreach ($ret[0] as $r) {
	$t2 += (1 + $r[1]-$r[0]);
}

echo "$t<br>\n";
echo "$t2<br>\n"; # 376411268753925 too high; 386427701078316 would therefore also be too high so not entered; 350513176553025 also too high; 
?>

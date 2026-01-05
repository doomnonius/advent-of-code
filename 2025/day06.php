<?php
$in = file('day06.input');
$input = [];
foreach ($in as $inp) $input[] = trim($inp);
$t = 0;
$t2 = 0;

# this is an ugly solution in my mind b/c it's hard-coded and not able to deal with a variable number of 
$i = array_map(null, preg_split('/\s+/', trim($input[0])), preg_split('/\s+/', trim($input[1])), preg_split('/\s+/', trim($input[2])), preg_split('/\s+/', trim($input[3])), preg_split('/\s+/', trim($input[4])));
foreach ($i as $a) {
	/* var_dump($a); */
	if ($a[4] == "+") $t += array_sum(array_slice($a,0,4));
	else $t += array_product(array_slice($a,0,4));
}
# part 2: i can use the operators to tell me where a stack begins
# find first non-space character in the operators row (ignoring the first one)
while (preg_match('/\s+/', trim($input[0]))) {
	# preg_split the last item in $input, then use the length of the longer part to substr negative that many from the other rows
	$ops = preg_split('/\s+/', $input[4]);
}
var_dump(preg_split('/\s+/', "9    9  8", 2));
echo "$t<br>\n";
echo "$t2<br>\n"; 
?>

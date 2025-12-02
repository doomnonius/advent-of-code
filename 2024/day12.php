<?php
class Coord {
	// Properties
	public $x;
	public $y;

	// Methods
	public function __construct($x,$y) {
		$this->x = $x;
		$this->y = $y;
	}
	
	public function neighbors() {
		return [new self($this->x+1, $this->y),new self($this->x, $this->y+1),new self($this->x-1,$this->y),new self($this->x, $this->y-1)];
	}
}

class Field {
	// Properties
	public $cont = [];
	public $peri = 0;
	public $proc = [];

	public function __construct($c) {
		$this->$proc[] = $c;
	}

	public function value() {
		return count($this->cont) * $this->peri;
	}

	public function map($c, $all_c, $visited) {
		return [[], []];
		$diffs = [];
		while count($this->proc) {
			$pos = array_pop($this->proc);
			$cont[] = $pos;
			foreach ($pos->neighbors as $n) {
				if (!in_array($n, $all_c)) { # all_c is not an array of coords
					$this->peri++;
				} else {
					if (!in_array($n, $this->cont)) {
						
					}
				}
			}
		}
		return [$diffs, $visited];
	}
}
# testing that ==  and in_array produce the answers I want
//$a = new Coord(0,0);
//$b = new Coord(1,1);
//$c = new Coord(0,0);
//$aC = [$a,$b];
//var_dump($a->neighbors());
//echo "<br>a=b? ".($a == $b)."<br>";
//echo "<br>a=c? ".($a == $c)."<br>";
//echo "<br>b=c? ".($b == $c)."<br>";
//echo "<br>c in aC? ".(in_array($c,$aC))."<br>";

$all_coords = [];
$input = file('/home/doomnonius/advent-of-code/2024/day12.input');
foreach ($input as $y => $l) {
	$chars = str_split($l);
	$all_coords[] = []; # I could say ...[$y] = [], but it'd be redundant
	foreach ($chars as $x => $c) {
		$all_coords[$y][] = $c; # same redundancy possible here
	}
}
# area * perimeter of each region
$to_visit = [new Field(new Coord(0,0))];
$visited = [];
$fields = [];
while (($f = array_pop($to_visit)) !==  null) {
	$a = $f->map($f->cont[0], $all_coords, $visited);
	$a[0] = $next;
	$a[1] = $visited;
	# this is not where I want to check in the coord is already in a field, but I need to remember to do that somewhere
	# foreach
}
var_dump($all_coords);

echo "end reached!";
?>

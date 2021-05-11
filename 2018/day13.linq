<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day13.input";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	List<Track> tracks = new List<Track>();
	List<Cart> carts = new List<Cart>();
	(tracks, carts) = buildTrack(ogdata);
	Console.WriteLine($"Part one: {part1(tracks, carts)}");
	Console.WriteLine($"Part two: {part2(tracks, carts)}"); // note that because I didn't deep copy these lists, you need to comment out part one to get the answer to part two
}

// Define other methods and classes here
public (int, int, int) part1(List<Track> tracks, List<Cart> carts)
{
	int count = 0;
	while (true)
	{
		carts.OrderBy(c => c.loc.y).ThenBy(d => d.loc.x);
		foreach (Cart cart in carts)
		{
			if (cart.loc.symbol == '+' && (cart.loc.east == null || cart.loc.west == null || cart.loc.north == null || cart.loc.south == null))
			{
				cart.loc.Dump("WARNING! + without four neighbors!");
			}
			cart.Move();
			//then check for overlap
			var locs = carts.GroupBy(c => c.loc);
			foreach (var grp in locs)
			{
				if (grp.Count() > 1)
				{
					//grp.Dump();
					return (grp.Key.x, grp.Key.y, count);
				}
			}
		}
		count++;
	}
}

public (int, int, int) part2(List<Track> tracks, List<Cart> carts)
{
	int count = 0;
	bool good = true;
	List<Cart> removal = new List<Cart>();
	while (good)
	{
		carts.OrderBy(c => c.loc.y).ThenBy(d => d.loc.x);
		if (carts.Count == 1) return (carts[0].loc.x, carts[0].loc.y, count);
		foreach (Cart cart in carts)
		{
			cart.Move();
			//then check for overlap
			var locs = carts.GroupBy(c => c.loc);
			foreach (var grp in locs)
			{
				if (grp.Count() > 1)
				{
					//grp.Dump();
					foreach (var car in grp)
					{
						//car.Dump();
						removal = carts.Where(c => c.loc == car.loc).ToList();
					}
				}
			}
		}
		if (removal.Count > 0)
		{
			foreach (Cart c in removal)
			{
				carts.Remove(carts.Where(d => d.loc == c.loc).ToList()[0]);
			}
			removal = new List<Cart>();
		}
		count++;
	}
	return (0, 0, 0);
}

public (List<Track>, List<Cart>) buildTrack (List<string> ogdata)
{
	List<Track> tracks = new List<Track>();
	List<Cart> carts = new List<Cart>();
	int row = 0;
	int column = 0;
	foreach (string line in ogdata)
	{
		char[] t = line.ToCharArray();
		foreach (char c in t)
		{
			// when creating, look left and up
			Track curr = new Track
			{
				x = column,
				y = row
			};
			if (c == ' ')
			{
				curr.symbol = c;
			}
			else if (c == '<' || c == '>' || c == '-')
			{
				Track w = tracks.Where(z => z.x == column - 1 && z.y == row).ToList()[0];
				curr.symbol = '-';
				curr.west = w;
				w.east = curr;
			}
			else if (c == '^' || c == 'v' || c == '|')
			{
				Track n = tracks.Where(z => z.x == column && z.y == row - 1).ToList()[0];
				curr.symbol = '|';
				curr.north = n;
				n.south = curr;
			}
			else if (c == '/') // either top left or bottom right
			{
				Track w = column == 0 ? null : tracks.Where(z => z.x == column - 1 && z.y == row).ToList()[0];
				Track n = row == 0 ? null : tracks.Where(z => z.x == column && z.y == row - 1).ToList()[0];
				curr.symbol = c;
				if ((w != null && n != null) && (w.symbol == '-' || w.symbol == '+') && (n.symbol == '|' || n.symbol == '+')) // then it is bottom right
				{
					curr.west = w;
					curr.north = n;
					w.east = curr;
					n.south = curr;
				}
				else { } // don't actually need to do anything
			}
			else if (c == '\\') // either top right or bottom left
			{
				Track w = column == 0 ? null : tracks.Where(z => z.x == column - 1 && z.y == row).ToList()[0];
				Track n = row == 0 ? null : tracks.Where(z => z.x == column && z.y == row - 1).ToList()[0];
				curr.symbol = c;
				if ((n != null) && (n.symbol == '|' || n.symbol == '+')) // then we are bottom left
				{
					curr.north = n;
					n.south = curr;
				}
				else
				{
					curr.west = w;
					w.east = curr;
				} // think we do nothing here too
			}
			else if (c == '+')
			{
				Track w = tracks.Where(z => z.x == column - 1 && z.y == row).ToList()[0];
				Track n = tracks.Where(z => z.x == column && z.y == row - 1).ToList()[0];
				curr.symbol = c;
				curr.north = n;
				curr.west = w;
				w.east = curr;
				n.south = curr;
			}
			tracks.Add(curr);
			// now create cart if neccesary
			if (c == '<')
			{
				Cart cart = new Cart
				{
					loc = curr,
					dir = 'w',
					next_turn = 0
				};
				carts.Add(cart);
			}
			else if (c == '>')
			{
				Cart cart = new Cart
				{
					loc = curr,
					dir = 'e',
					next_turn = 0
				};
				carts.Add(cart);
			}
			else if (c == 'v')
			{
				Cart cart = new Cart
				{
					loc = curr,
					dir = 's',
					next_turn = 0
				};
				carts.Add(cart);
			}
			else if (c == '^')
			{
				Cart cart = new Cart
				{
					loc = curr,
					dir = 'n',
					next_turn = 0
				};
				carts.Add(cart);
			}

			column++;
		}
		row++;
		column = 0;
	}
	return (tracks, carts);
}

public class Track
{
	public int x { get; set; }
	public int y { get; set; }
	public char symbol { get; set; }
	public Track north { get; set; }
	public Track east { get; set; }
	public Track south { get; set; }
	public Track west { get; set; }
}

public class Cart
{
	public Track loc { get; set; }
	public char dir { get; set; } // n, e, s, w
	public int next_turn { get; set; } // this is 0, 1, or 2

	public void Move()
	{
		Track last_loc = this.loc;
		if (this.loc.symbol == '-' || this.loc.symbol == '|') // need to make sure I turn things properly or this will break
		{
			if (this.dir == 'n') this.loc = this.loc.north;
			else if (this.dir == 's') this.loc = this.loc.south;
			else if (this.dir == 'w') this.loc = this.loc.west;
			else if (this.dir == 'e') this.loc = this.loc.east;
		}
		else if (this.loc.symbol == '/') // can intuit top left or bottom right based on direction
		{
			if (this.dir == 'n') 
			{
				this.dir = 'e';
				this.loc = this.loc.east;
			}
			else if (this.dir == 's')
			{
				this.dir = 'w';
				this.loc = this.loc.west;
			}
			else if (this.dir == 'w')
			{
				this.dir = 's';
				this.loc = this.loc.south;
			}
			else if (this.dir == 'e')
			{
				this.dir = 'n';
				this.loc = this.loc.north;
			}
		}
		else if (this.loc.symbol == '\\') // can intuit top right or bottom left based on direction
		{
			if (this.dir == 's')
			{
				this.dir = 'e';
				this.loc = this.loc.east;
			}
			else if (this.dir == 'n')
			{
				this.dir = 'w';
				this.loc = this.loc.west;
			}
			else if (this.dir == 'e')
			{
				this.dir = 's';
				this.loc = this.loc.south;
			}
			else if (this.dir == 'w')
			{
				this.dir = 'n';
				this.loc = this.loc.north;
			}
		}
		else if (this.loc.symbol == '+')
		{
			List<char> north_turns = new List<char> { 'w', 'n', 'e' };
			List<Track> north_locs = new List<Track> { this.loc.west, this.loc.north, this.loc.east };
			List<char> south_turns = new List<char> { 'e', 's', 'w' };
			List<Track> south_locs = new List<Track> { this.loc.east, this.loc.south, this.loc.west };
			List<char> east_turns = new List<char> { 'n', 'e', 's' };
			List<Track> east_locs = new List<Track> { this.loc.north, this.loc.east, this.loc.south };
			List<char> west_turns = new List<char> { 's', 'w', 'n' };
			List<Track> west_locs = new List<Track> { this.loc.south, this.loc.west, this.loc.north };
			if (this.dir == 's')
			{
				this.dir = south_turns[this.next_turn];
				this.loc = south_locs[this.next_turn];
			}
			else if (this.dir == 'n')
			{
				this.dir = north_turns[this.next_turn];
				this.loc = north_locs[this.next_turn];
			}
			else if (this.dir == 'e')
			{
				this.dir = east_turns[this.next_turn];
				this.loc = east_locs[this.next_turn];
			}
			else if (this.dir == 'w')
			{
				this.dir = west_turns[this.next_turn];
				this.loc = west_locs[this.next_turn];
			}
			this.next_turn = (this.next_turn + 1) % 3;
		}
		if (this.loc == null)
		{
			last_loc.Dump("WARNING! Null location");
		}
	}
}
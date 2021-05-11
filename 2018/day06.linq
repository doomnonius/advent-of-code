<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day06.input";
	//string ogtestData = "1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	//List<string> testData = ogtestData.Split('\n').ToList();
	List<Coord> data = new List<Coord>();
	foreach (string c in ogdata)
	{
		string[] splits = c.Split(',');
		data.Add(new Coord 
			{
				x = Int32.Parse(splits[0]),
				y = Int32.Parse(splits[1])
			}
		);
	}
	int x_min = data.Min(c => c.x);
	int x_max = data.Max(c => c.x);
	int y_min = data.Min(c => c.y);
	int y_max = data.Max(c => c.y);
	List<Coord> edges = new List<Coord> ();
	List<Coord> full_area = calcArea(x_min-1, x_max+1, y_min-1, y_max+1, data, out edges);
	//edges.Dump("Edges");
	//full_area.Dump("Area");
	Console.WriteLine($"Part one: {part1(data, full_area, edges)}"); // not 4632, too high; nor 4623
	Console.WriteLine($"Part two: {part2(data, full_area, 10000)}");
}

// Define other methods and classes here
public int part1 (List<Coord> points, List<Coord> rel_area, List<Coord> edges)
{
	Dictionary<Coord, int> c_dict = new Dictionary<Coord, int>();
	Coord equi = new Coord { x = -1, y = -1 };
	c_dict.Add(equi, 0);
	foreach (Coord c in points)
	{
		c_dict.Add(c, 0);
	}
	foreach (Coord p in rel_area)
	{
		int min = 1000;
		Coord nearest = equi;
		foreach (Coord c in points)
		{
			int man = manhattan(c, p);
			if (man < min)
			{
				min = man;
				nearest = c;
			} else if (man == min)
			{
				nearest = equi;
			}
		}
		if (!edges.Contains(p))
		{
			c_dict[nearest]++;
		} else {
			c_dict[nearest] = 100000;
		}
	}
	return c_dict.Where(z => z.Value < 100000).Max(a => a.Value);
}

public int part2(List<Coord> points, List<Coord> rel_area, int maxDist)
{
	int retVal = 0;
	foreach (Coord p in rel_area)
	{
		int totalManhattan = 0;
		foreach (Coord c in points)
		{
			totalManhattan += manhattan(c, p);
		}
		if (totalManhattan < maxDist)
		{
			retVal += 1;
		}
	}
	return retVal;
}

public List<Coord> calcArea (int x_min, int x_max, int y_min, int y_max, List<Coord> existing, out List<Coord> edges)
{
	List<Coord> retVal = new List<Coord> ();
	List<Coord> all_edges = new List<Coord> ();
	for (int cx = x_min; cx <= x_max; cx++)
	{
		for (int cy = y_min; cy <= y_max; cy++)
		{
			Coord newVal = new Coord {x = cx, y = cy};
			retVal.Add(newVal);
			if (cx == x_min || cy == y_min || cx == x_max || cy == y_max)
			{
				all_edges.Add(newVal);
			}
		}
	}
	edges = all_edges;
	return retVal;
}

public int manhattan (Coord p1, Coord p2)
{
	return (Math.Abs(p1.x-p2.x) + Math.Abs(p1.y-p2.y));
}

class CoordComparer : IEqualityComparer<Coord>
{
	public bool Equals(Coord a, Coord b)
	{
		if (Object.ReferenceEquals(a, b)) return true;

		if (Object.ReferenceEquals(a, null) || Object.ReferenceEquals(b, null)) return false;

		return a.x == b.x && a.y == b.y;
	}

	public int GetHashCode(Coord c)
	{
		if (Object.ReferenceEquals(c, null)) return 0;

		int hashCoordX = c.x.GetHashCode();
		int hashCoordY = c.y.GetHashCode();

		return hashCoordX ^ hashCoordY;
	}
}

public class Coord : IEquatable<Coord>
{
	public int x { get; set; }
	public int y { get; set; }

	public bool Equals(Coord other)
	{
		//Console.WriteLine("Are we even getting here?");
		if (other.x == this.x && other.y == this.y) return true;
		else return false;
	}
}
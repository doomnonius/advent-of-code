<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day10.input";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	List<Coord> lights = new List<Coord>();
	foreach (string line in ogdata)
	{
		int first_open = line.IndexOf("<");
		int first_close = line.IndexOf(">") - first_open;
		string pos = line.Substring(first_open + 1, first_close - 1);
		List<int> coords = pos.Split(',').ToList().ConvertAll(x => Int32.Parse(x));
		int last_open = line.LastIndexOf("<");
		int last_close = line.LastIndexOf(">") - last_open;
		string vel = line.Substring(last_open + 1, last_close - 1);
		List<int> vels = vel.Split(',').ToList().ConvertAll(x => Int32.Parse(x));
		lights.Add( new Coord
			{
				x = coords[0],
				y = coords[1],
				vel_x = vels[0],
				vel_y = vels[1]
			}
		);
	}
	//lights.Dump();
	Console.WriteLine($"Part one: {part1(lights)}");
	//Console.WriteLine($"Part two: {}");
}

// Define other methods and classes here
public string part1 (List<Coord> lights)
{
	int i = 0;
	while (true)
	{
		long curr_area = calcArea(lights);
		foreach (Coord light in lights)
		{
			light.Move();
		}
		long next_area = calcArea(lights);
		i++;
		if (next_area == 549) // I had some simple code that figured out that this was the minimum size the lights converged too
		{
			displayMap(lights);
			Console.WriteLine($"Part two: {i}");
			break;
		}
	}
	return "See console";
}

public long calcArea (List<Coord> lights)
{
	long width = lights.Max(z => z.x) - lights.Min(z => z.x);
	long height = lights.Max(z => z.y) - lights.Min(z => z.y);
	//Console.WriteLine($"{width}");
	return width * height;
}

public void displayMap(List<Coord> lights)
{
	for (int y = lights.Min(z => z.y); y <= lights.Max(z => z.y); y++)
	{
		for (int x = lights.Min(z => z.x); x <= lights.Max(z => z.x); x++)
		{
			if (lights.Contains(new Coord { x = x, y = y }, new CoordComparer()))
			{
				Console.Write(".");
			}
			else
			{
				Console.Write(" ");
			}
		}
		Console.WriteLine();
	}
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
	public int vel_x { get; set; }
	public int vel_y { get; set; }
	
	public void Move ()
	{
		this.x += this.vel_x;
		this.y += this.vel_y;
	}
	
	public bool Equals(Coord other)
	{
		//Console.WriteLine("Are we even getting here?");
		if (other.x == this.x && other.y == this.y) return true;
		else return false;
	}
}
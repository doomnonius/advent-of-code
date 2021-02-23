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
	}
	//Console.WriteLine($"Part one: {}");
	//Console.WriteLine($"Part one: {}");
}

// Define other methods and classes here
public void part1 ()
{
	
}



//class CoordComparer : IEqualityComparer<Coord>
//{
//	public bool Equals(Coord a, Coord b)
//	{
//		if (Object.ReferenceEquals(a, b)) return true;
//
//		if (Object.ReferenceEquals(a, null) || Object.ReferenceEquals(b, null)) return false;
//
//		return a.x == b.x && a.y == b.y;
//	}
//
//	public int GetHashCode(Coord c)
//	{
//		if (Object.ReferenceEquals(c, null)) return 0;
//
//		int hashCoordX = c.x.GetHashCode();
//		int hashCoordY = c.y.GetHashCode();
//
//		return hashCoordX ^ hashCoordY;
//	}
//}

public class Coord //: IEquatable<Coord>
{
	public int x { get; set; }
	public int y { get; set; }
	
	public int vel_x { get; set; }
	public int vel_y { get; set; }
	
	//public bool Equals(Coord other)
	//{
	//	//Console.WriteLine("Are we even getting here?");
	//	if (other.x == this.x && other.y == this.y) return true;
	//	else return false;
	//}
}
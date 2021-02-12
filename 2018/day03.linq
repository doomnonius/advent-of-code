<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day03.input";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	
	List<FabricSection> data = new List<FabricSection> ();
	foreach (string square in ogdata)
	{
		List<string> x = square.Split().ToList();
		//x.Dump();
		int commaIndex = x[2].IndexOf(",");
		int colonIndex = x[2].IndexOf(":");
		int xIndex = x[3].IndexOf("x");
		data.Add(
			new FabricSection {
				id = Int32.Parse(x[0].Substring(1)),
				leftOffset = Int32.Parse(x[2].Substring(0, commaIndex)),
				topOffset = Int32.Parse(x[2].Substring(commaIndex + 1, colonIndex - commaIndex -1)),
				width = Int32.Parse(x[3].Substring(0, xIndex)),
				height = Int32.Parse(x[3].Substring(xIndex + 1))
			}
		);
		//data.Dump();
	}
	
	Console.WriteLine($"Part one: {part1(data)}");
	//Console.WriteLine($"Part two: {part2(data)}");
}

// Define other methods and classes here
public int part1 (List<FabricSection> squares) {
	//squares.Dump();
	//int retVal = 0;
	List<Coord> overlaps = new List<Coord> ();
	List<List<Coord>> squareLayouts = new List<List<Coord>> ();
	List<int> ids = (from s in squares select s.id).ToList();
	foreach (FabricSection square in squares)
	{
		List<Coord> newCoords = squareCoords(square);
		squareLayouts.Add(newCoords);
	}
	int i = 1;
	foreach (List<Coord> squareCoords in squareLayouts)
	{
		int j = 1;
		//Console.WriteLine($"Progress: {i}/{squareLayouts.Count}");
		foreach (List<Coord> squareCoords2 in squareLayouts.GetRange(i, squareLayouts.Count - i))
		{
			List<Coord> overlap = squareCoords.Intersect(squareCoords2, new CoordComparer()).ToList();
			//overlap.Dump();
			if (overlap.Count > 0)
			{
				ids.Remove(i); // i will equal squareCoords
				ids.Remove(i + j); // j will equal sqareCoords2
			}
			foreach (Coord c in overlap)
			{
				if (overlaps.Contains(c))
				{
					
				}
				else
				{
					overlaps.Add(c);
				}
			}
			j++;
		}
		i++;
	}
	ids.Dump("Part 2:");
	return overlaps.Count;
}

public List<Coord> squareCoords (FabricSection fabric) {
	List<Coord> retVal = new List<Coord> ();
	for (int i = fabric.leftOffset; i < fabric.leftOffset + fabric.width; i++)
	{
		for (int j = fabric.topOffset; j < fabric.topOffset + fabric.height; j++)
		{
			retVal.Add(new Coord {x = i, y = j} );
		}
	}
	//retVal.Dump();
	return retVal;
}

class CoordComparer : IEqualityComparer<Coord>
{
	public bool Equals (Coord a, Coord b)
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
	
	public bool Equals (Coord other)
	{
		//Console.WriteLine("Are we even getting here?");
		if (other.x == this.x && other.y == this.y) return true;
		else return false;
	}
}

public class FabricSection
{
	public int id { get; set; }
	public int leftOffset { get; set; }
	public int topOffset { get; set; }
	public int width { get; set; }
	public int height { get; set; }
}
<Query Kind="Program" />

void Main()
{
	int serial = 6548;
	List<FuelCell> grid = calcCells(serial);
	Console.WriteLine($"Part one: {part1(grid)}");
	Console.WriteLine($"Part two: {calcBestCharge(90, 269, 18, 300, 300)}");
	Console.WriteLine($"Part two: {part2(serial, 300, 300)}"); // This one needs a lot of optimizing. 233,250,12 but it took 13:53 to find --> down to 3:16
}

// Define other methods and classes here
public List<FuelCell> calcCells (int serial)
{
	List<FuelCell> grid = new List<FuelCell>();
	for (int y = 1; y <= 298; y++)
	{
		for (int x = 1; x <= 298; x++)
		{
			grid.Add( new FuelCell
				{
					x = x,
					y = y,
					charge = calcCharge(x, y, serial) + calcCharge(x+1, y, serial) + calcCharge(x+2, y, serial) + calcCharge(x, y+1, serial) + calcCharge(x, y+2, serial) + calcCharge(x+1, y+1, serial) + calcCharge(x+1, y+2, serial) + calcCharge(x+2, y+1, serial) + calcCharge(x+2, y+2, serial)
				}
			);
		}
	}
	return grid;
}

public (int, int, int, int) part2 (int serial, int x_max, int y_max)
{
	List<FuelCell2> grid = new List<FuelCell2>();
	for (int y = 1; y <= y_max; y++)
	{
		for (int x = 1; x <= x_max; x++)
		{
			(int c, int s) = calcBestCharge(x, y, serial, x_max, y_max);
			//Console.WriteLine($"Calculating best charge for ({x}, {y})");
			grid.Add(new FuelCell2
				{
					x = x,
					y = y,
					charge = c,
					size = s
				}
			);
		}
	}
	int m = grid.Max(z => z.charge);
	FuelCell2 retVal = grid.Where(a => a.charge == m).ToList()[0];
	return (retVal.x, retVal.y, retVal.size, retVal.charge);
}

public (int, int) part1 (List<FuelCell> cells)
{
	int m = cells.Max(z => z.charge);
	FuelCell retVal = cells.Where(a => a.charge == m).ToList()[0];
	return (retVal.x, retVal.y);
}

public (int, int) calcBestCharge(int x, int y, int serial, int x_max, int y_max)
{
	int max_square = new List<int> { x_max + 1 - x, y_max + 1 - y }.Min();
	//Console.WriteLine($"max_square: {max_square}");
	int m = -100000;
	int s = 0;
	int tempVal = 0;
	for (int c = 1; c <= max_square; c++)
	{
		for (int a = 0; a < c; a++)
		{
			for (int b = 0; b < c; b++)
			{
				if (a == c-1 || b == c-1) tempVal += calcCharge(x + a, y + b, serial);
				//Console.WriteLine($"{tempVal}");
			}
		}
		//Console.WriteLine($"tempVal at size {c}: {tempVal}");
		if (tempVal > m)
		{
			//Console.WriteLine("New max.");
			m = tempVal;
			s = c;
		}
	}
	return (m, s);
}

public int calcCharge (int x, int y, int serial)
{
	int rackId = x + 10;
	int power_lvl = rackId * y;
	power_lvl += serial;
	power_lvl *= rackId;
	power_lvl = (power_lvl / 100) % 10;
	power_lvl -= 5;
	return power_lvl;
}

public class FuelCell
{
	public int x { get; set; }
	public int y { get; set; }
	public int charge { get; set; }
	
	public int threeby (List<FuelCell> cells)
	{
		int right1 = cells.Where(z => z.x == this.x+1 && z.y == this.y).ToList()[0].charge;
		int right2 = cells.Where(z => z.x == this.x+2 && z.y == this.y).ToList()[0].charge;
		int down1 = cells.Where(z => z.y == this.y+1 && z.x == this.x).ToList()[0].charge;
		int down2 = cells.Where(z => z.y == this.y+1 && z.x == this.x).ToList()[0].charge;
		int r1d1 = cells.Where(z => z.y == this.y+1 && z.x == this.x+1).ToList()[0].charge;
		int r2d1 = cells.Where(z => z.y == this.y+1 && z.x == this.x+2).ToList()[0].charge;
		int r1d2 = cells.Where(z => z.y == this.y+2 && z.x == this.x+1).ToList()[0].charge;
		int r2d2 = cells.Where(z => z.y == this.y+2 && z.x == this.x+2).ToList()[0].charge;
		return this.charge + right1 + right2 + down1 + down2 + r1d1 + r1d2 + r2d1 + r2d2;
	}
}

public class FuelCell2
{
	public int x { get; set; }
	public int y { get; set; }
	public int charge { get; set; }
	public int size { get; set; }
}
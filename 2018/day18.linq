<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day18.input";
	string[] ogdata = File.ReadAllText(filePath).Split('\n');
	char[,] data = new char[ogdata.Length, ogdata[0].Trim().Length];
	for (int i = 0; i < ogdata.Length; i++)
	{
		char[] line = ogdata[i].Trim().ToArray();
		for (int j = 0; j < line.Length; j++)
		{
			data[i,j] = line[j];
		}
	}
	//data.Dump();
	char[,] dataCopy = (char[,]) data.Clone();
	Console.WriteLine($"Part one: {part1(dataCopy, 10)}"); // not 259128, too low; also, have to commen out line one to solve line two properly
	Console.WriteLine($"Part two: {part2(data, 1000000000)}"); // finding a loop, then extrapolating; not 193120, too low; not 211140, too high; 208351 also too high; not 207172;
}

// You can define other methods, fields, classes and namespaces here
public int part1 (char[,] area, int loops)
{
	int height = area.GetLength(0);
	int width = area.GetLength(1);
	Dictionary<char, char> nextChar = new Dictionary<char, char> {
		{'.', '|'},
		{'|', '#'},
		{'#', '.'}
	};
	while (loops > 0)
	{
		char[,] new_area = new char[height, width];
		for (int y = 0; y < height; y++)
		{
			for (int x = 0; x < width; x++)
			{
				char point = area[y, x];
				if (countNeighbors(x, y, point, area)) new_area[y,x] = nextChar[point];
				else new_area[y,x] = point;
			}
		}
		area = new_area;
		loops--;
	}
	return resourceValue(area);
}

public int part2(char[,] area, int loops)
{
	int height = area.GetLength(0);
	int width = area.GetLength(1);
	Dictionary<int, int> prev = new Dictionary<int, int>();
	Dictionary<char, char> nextChar = new Dictionary<char, char> {
		{'.', '|'},
		{'|', '#'},
		{'#', '.'}
	};
	List<int> prevPatt = new List<int>();
	while (loops > 0) //193120
	{
		char[,] new_area = new char[height, width];
		for (int y = 0; y < height; y++)
		{
			for (int x = 0; x < width; x++)
			{
				char point = area[y, x];
				if (countNeighbors(x, y, point, area)) new_area[y, x] = nextChar[point];
				else new_area[y, x] = point;
			}
		}
		area = new_area;
		//area.Dump();
		loops--;
		if (loops > 100000000) // identify the loop in some way and extrapolate
		{
			int prevRV = resourceValue(area);
			if (prev.Keys.Contains(prevRV))
			{
				int loopStart = prev[prevRV];
				int loopEnd = loops + 1;
				List<int> newPatt = prev.Where(x => x.Value <= loopStart && x.Value >= loopEnd).OrderByDescending(x => x.Value).Select(x => x.Key).ToList();
				if (newPatt.Count == prevPatt.Count)
				{
					int remaining = prev[newPatt[0]]; // number of loops left
					return newPatt[remaining % newPatt.Count];
				}
				prevPatt = newPatt.ConvertAll(x => x);
				prev[prevRV] = loops;
			}
			else prev.Add(prevRV, loops);
		}
	}
	return resourceValue(area);
}

public bool countNeighbors(int x, int y, char key, char[,] area)
{
	List<char> neighbors = new List<char> {};
	int h = area.GetLength(0);
	int w = area.GetLength(1);
	int lineCount = 0;
	int octoCount = 0;
	for (int xx = -1; xx <= 1; xx++)
	{
		for (int yy = -1; yy <= 1; yy++)
		{
			if (xx == 0 && yy == 0)
			{
				continue;
			}
			if (x + xx >= 0 && y + yy >= 0 && x + xx < w && y + yy < h)
			{
				if (area[y+yy,x+xx] == '.') continue;
				else if (area[y+yy,x+xx] == '|') lineCount++;
				else if (area[y+yy,x+xx] == '#') octoCount++;
			}
		}
	}
	if (key == '.' && lineCount >= 3) return true;
	else if (key == '|' && octoCount >= 3) return true;
	else if (key == '#' && (octoCount < 1 || lineCount < 1)) return true;
	return false;
}

public int resourceValue (char[,] area)
{
	int woods = 0;
	int yards = 0;
	foreach (char c in area)
	{
		if (c == '|') woods++;
		else if (c == '#') yards++;
	}
	return woods * yards;
}

public bool checkMatch(List<int> a, List<int> b)
{
	bool retVal = true;
	if (a.Count != b.Count)
	{
		return false;
	}
	for (int x = a.Count - 1; x >= 0; x--)
	{
		if (a[x] != b[x])
		{
			retVal = false;
			break;
		}
	}
	return retVal;
}
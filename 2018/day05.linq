<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day05.input";
	List<char> data = File.ReadAllText(filePath).ToList();
	Console.WriteLine($"Part one: {part1(data)}"); // 28418 is too high; 
	Console.WriteLine($"Part two: {part2(data)}");
}

// Define other methods and classes here
public int part1 (List<char> formula)
{
	bool broken = false;
	while (true)
	{
		for (int i = 0; i < formula.Count-1; i++)
		{
			if ((Char.IsUpper(formula[i]) && Char.IsLower(formula[i+1]) && formula[i] == Char.ToUpper(formula[i+1])) || (Char.IsLower(formula[i]) && Char.IsUpper(formula[i+1]) && Char.ToUpper(formula[i]) == formula[i+1]))
			{
				formula.RemoveAt(i + 1);
				formula.RemoveAt(i);
				broken = true;
				break;
			}
		}
		if (broken)
		{
			broken = false;
			continue;
		}
		//formula.Dump();
		return formula.Count;
	}
}

public int part2(List<char> formula)
{
	int m = 9390;
	foreach (char c in formula.ConvertAll(x => Char.ToUpper(x)).Distinct())
	{
		List<char> formula2 = new List<char>(formula.Count);
		formula.ForEach((item) =>
		{
			formula2.Add(item);
		});
		formula2.RemoveAll(x => x == c || x == Char.ToLower(c));
		int next = part1(formula2);
		if (next < m) m = next;
	}
	return m;
}
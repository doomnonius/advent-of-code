<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day12.input";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	string initial_state = ogdata[0].Substring(ogdata[0].IndexOf(":")+2);
	initial_state.Dump();
	List<string> r = ogdata.GetRange(2, ogdata.Count - 2);
	List<Rule> rules = new List<Rule>();
	foreach (string rule in r)
	{
		rules.Add( new Rule
			{
				pattern = rule.Substring(0, 5),
				result = rule.Trim().Last().ToString()
			}
		);
	}
	Console.WriteLine($"Part one: {part1(20, initial_state, rules)}"); // not 315, too low
	Console.WriteLine($"Part two: {part2()}"); // brute forcing again - actually, figured out the shortcut by hand, which is kind of cheating
}

// Define other methods and classes here
public int part1 (long gen, string plants, List<Rule> rules)
{
	int retVal = 0;
	int i = 0;
	int added = 0;
	while (i < gen)
	{
		int p = plants.IndexOf("#");
		if (p < 3) 
		{ 
			for (int j = 0; j < 3-p; j++) 
			{
				plants = plants.Insert(0, ".");
				added++;
			}
		}
		else if (p > 5)
		{
			plants = plants.Substring(2);
			added -= 2;
		}
		for (int j = 3; j > 0; j--) plants = plants.Insert(plants.Length-1, ".");
		string new_plants = " ".Insert(0, plants.Substring(0, 2));
		for (int j = 0; j < plants.Length - 5; j++)
		{
			string curr = plants.Substring(j, 5);
			foreach (Rule r in rules)
			{
				if (r.pattern == curr)
				{
					new_plants = new_plants.Insert(new_plants.Length-1, r.result);
					//plants.Dump();
					break;
				}
			}
		}
		i++;
		if (i % 1000 == 0)
		{
			new_plants.Dump($"{i}, added: {added}");
		}
		plants = new_plants;
	}
	plants.Dump();
	int score = 0 - added;
	foreach (char c in plants.ToCharArray())
	{
		if (c == '#')
		{
			retVal += score;
		}
		score++;
	}
	return retVal;
}

public long part2 ()
{
	long retVal = 0;
	long score = 0 + (50000000000 - 76);
	foreach (char c in ".....#...............#.........................#....#....#.......#.......#....#.....#....#.......#.......#.......#.....#....#....#.......#....#.......#.......#.......#.....#...".ToCharArray())
	{
		if (c == '#')
		{
			retVal += score;
		}
		score++;
	}
	return retVal;
}

public class Rule
{
	public string pattern { get; set; }
	public string result { get; set; }
}
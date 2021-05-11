<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day16.input";
	List<string> ogdata = File.ReadAllText(filePath).Split("cc").ToList();
	List<string> testCases = ogdata[0].Split("c").ToList();
	List<beforeAfter> cases = new List<beforeAfter>();
	foreach (string c in testCases)
	{
		string[] lines = c.Split('\n');
		cases.Add( new beforeAfter
			{
				before = lines[0].Substring(9, lines[0].Length - 11).Split(',').ToList().ConvertAll(x => Int32.Parse(x)),
				command = lines[1].Split(' ').ToList().ConvertAll(x => Int32.Parse(x)),
				after = lines[2].Substring(9, lines[0].Length - 11).Split(',').ToList().ConvertAll(x => Int32.Parse(x))
			}
		);
	}
	Dictionary<int, List<string>> posses;
	Console.WriteLine($"Part one: {part1(cases, out posses)}"); // not 231, too low
	List<List<int>> program = ogdata[1].Split('\n').ToList().ConvertAll(x => x.Split(' ').ToList().ConvertAll(y => Int32.Parse(y)));
	Console.WriteLine($"Part two: {part2(program, posses)}"); // part of this will be reducing the possibilities
}

// You can define other methods, fields, classes and namespaces here
public int part2(List<List<int>> program, Dictionary<int, List<string>> poss)
{
	//first find what each one corresponds to
	Dictionary<int, string> matches = new Dictionary<int, string>();
	Dictionary<string, Func<List<int>, List<int>, List<int>>> corresponds = new Dictionary<string, Func<List<int>, List<int>, List<int>>>
	{
		{"addr", addr},
		{"addi", addi},
		{"mulr", mulr},
		{"muli", muli},
		{"banr", banr},
		{"bani", bani},
		{"borr", borr},
		{"bori", bori},
		{"setr", setr},
		{"seti", seti},
		{"gtir", gtir},
		{"gtri", gtri},
		{"gtrr", gtrr},
		{"eqir", eqir},
		{"eqri", eqri},
		{"eqrr", eqrr}
	};
	while (poss.Keys.Count > 0)
	{
		foreach (int k in poss.Keys)
		{
			if (poss[k].Count == 1)
			{
				string r = poss[k][0];
				matches[k] = r;
				foreach (List<string> L in poss.Values)
				{
					if (L.Contains(r)) L.Remove(r);
				}
				poss.Remove(k);
			}
		}
	}
	matches.OrderBy(x => x.Key).Dump();
	List<int> registers = new List<int> {0, 0, 0, 0};
	foreach (List<int> command in program)
	{
		registers = corresponds[matches[command[0]]](command, registers);
	}
	return registers[0];
}

public int part1 (List<beforeAfter> cases, out Dictionary<int, List<string>> possibilities)
{
	int retVal = 0;
	Dictionary<int, List<string>> poss = new Dictionary<int, List<string>> ();
	for (int i = 0; i <= 15; i++)
	{
		poss.Add(i, new List<string>());
	}
	foreach (beforeAfter line in cases)
	{
		int count = 0;
		List<string> subPoss = new List<string>();
		//addr
		List<int> result = addr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("addr"); count++;
		//addi
		result = addi(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("addi"); count++;
		//mulr
		result = mulr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("mulr"); count++;
		//muli
		result = muli(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("muli"); count++;
		//banr
		result = banr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("banr"); count++;
		//bani
		result = bani(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("bani"); count++;
		//borr
		result = borr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("borr"); count++;
		//bori
		result = bori(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("bori"); count++;
		//setr
		result = setr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("setr"); count++;
		//seti
		result = seti(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("seti"); count++;
		//gtir
		result = gtir(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("gtir"); count++;
		//gtri
		result = gtri(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("gtri"); count++;
		//gtrr
		result = gtrr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("gtrr"); count++;
		//eqir
		result = eqir(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("eqir"); count++;
		//eqri
		result = eqri(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("eqri"); count++;
		//eqrr
		result = eqrr(line.command, line.before);
		if (checkMatch(result, line.after)) subPoss.Add("eqrr"); count++;
		if (poss[line.command[0]].Count < 1) poss[line.command[0]] = subPoss.ConvertAll(x => x);
		if (count > 2) retVal++;
	}
	possibilities = poss;
	return retVal;
}

public List<int> addi(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);  //quick 'n' easy deep copy
	result[commands[3]] = before[commands[1]] + commands[2];
	return result;
}

public List<int> mulr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] * before[commands[2]];
	return result;
}

public List<int> muli(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] * commands[2];
	return result;
}

public List<int> banr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] & before[commands[2]];
	return result;
}

public List<int> bani(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] & commands[2];
	return result;
}

public List<int> borr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] | before[commands[2]];
	return result;
}

public List<int> bori(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] | commands[2];
	return result;
}

public List<int> setr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]];
	return result;
}

public List<int> seti(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = commands[1];
	return result;
}

public List<int> gtir(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = commands[1] > before[commands[2]] ? 1 : 0;
	return result;
}

public List<int> gtri(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] > commands[2] ? 1 : 0;
	return result;
}

public List<int> gtrr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] > before[commands[2]] ? 1 : 0;
	return result;
}

public List<int> eqir (List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = commands[1] == before[commands[2]] ? 1 : 0;
	return result;
}

public List<int> eqri (List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] == commands[2] ? 1 : 0;
	return result;
}

public List<int> eqrr (List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] == before[commands[2]] ? 1 : 0;
	return result;
}

public List<int> addr (List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[3]] = before[commands[1]] + before[commands[2]];
	return result;
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

public class beforeAfter
{
	public List<int> before { get; set; }
	public List<int> command { get; set; }
	public List<int> after { get; set; }
}
<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day21.input";
	string[] ogdata = File.ReadAllText(filePath).Split('\n');
	Dictionary<int, (string, List<int>)> commands = new Dictionary<int, (string, List<int>)>();
	int ind = 0;
	foreach (string line in ogdata.ToList().GetRange(1, ogdata.Length - 1))
	{
		List<string> splitLine = line.Split(' ', 2).ToList();
		commands.Add(ind, (splitLine[0], splitLine[1].Split(' ').ToList().ConvertAll(x => Int32.Parse(x))));
		ind++;
	}
	part1(ogdata[0].Trim(), commands);
	//Console.WriteLine($"Part two: {part2(ogdata[0].Trim(), commands)}");
}

// You can define other methods, fields, classes and namespaces here
public void part1(string ipData, Dictionary<int, (string, List<int>)> program)
{
	Dictionary<int, int> retVal = new Dictionary<int, int> ();
	//for (int i = 10626258; i <= 12361563; i++)
	//{
	//	//$"Running with {i} in index 0.".Dump();
	runCode(ipData, program, 0);
	//	if (r > 0)
	//	{
	//		$"Returned {r}".Dump();
	//		retVal.Add(i, r);
	//	}
	//}
	//return retVal.Where(x => x.Value == retVal.Min(y => y.Value)).ToList()[0];
}


public long runCode(string ipData, Dictionary<int, (string, List<int>)> program, int reg1)
{
	//reg1.Dump();
	bool p1 = true;
	int ip = 0;
	int runs = 0;
	int ipIndex = Int32.Parse(ipData.Substring(ipData.LastIndexOf(' ') + 1));
	Dictionary<string, Func<List<int>, List<long>, List<long>>> opcodes = new Dictionary<string, Func<List<int>, List<long>, List<long>>>
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
	List<long> registers = new List<long> { reg1, 0, 0, 0, 0, 0 };
	List<long> options = new List<long> ();
	while (ip < program.Count)
	{
		List<int> command = program[ip].Item2;
		registers[ipIndex] = ip;
		//registers.Dump();
		registers = opcodes[program[ip].Item1](command, registers);
		ip = Convert.ToInt32(registers[ipIndex]);
		//ip.Dump();
		if (ip == 12)
		{
			registers.Dump();
			break;
		}
		ip++;
		//program[ip].Item1.Dump();
		runs++;
		if (program[ip].Item1 == "eqrr")
		{
			if (p1)
			{
				Console.WriteLine($"Part one: {registers[4]}");
				registers.Dump();
				p1 = false;
			}
			if (options.Contains(registers[4]))
			{
				Console.WriteLine($"Part two: {options.Last()}");
				return 0;
			}
			else
			{
				options.Add(registers[4]);
			}
		}
		//runs.Dump();
	}
	return 0;
	//if (limiter < 49)
	//{
	//	return runs;
	//}
	//else
	//{
	//	return 0;
	//}
}

public List<long> addi(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);  //quick 'n' easy deep copy
	result[commands[2]] = before[commands[0]] + commands[1];
	return result;
}

public List<long> mulr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] * before[commands[1]];
	return result;
}

public List<long> muli(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	//$"{commands[1]} * {before[commands[0]]}".Dump();
	//$"{commands[1] * before[commands[0]]}".Dump();
	result[commands[2]] = before[commands[0]] * commands[1];
	return result;
}

public List<long> banr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] & before[commands[1]];
	return result;
}

public List<long> bani(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	//result.Dump();
	result[commands[2]] = before[commands[0]] & commands[1];
	//result.Dump();
	return result;
}

public List<long> borr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] | before[commands[1]];
	return result;
}

public List<long> bori(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] | Convert.ToInt64(commands[1]);
	return result;
}

public List<long> setr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]];
	return result;
}

public List<long> seti(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = commands[0];
	return result;
}

public List<long> gtir(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = commands[0] > before[commands[1]] ? 1 : 0;
	return result;
}

public List<long> gtri(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] > commands[1] ? 1 : 0;
	return result;
}

public List<long> gtrr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] > before[commands[1]] ? 1 : 0;
	return result;
}

public List<long> eqir(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = commands[0] == before[commands[1]] ? 1 : 0;
	return result;
}

public List<long> eqri(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] == commands[1] ? 1 : 0;
	return result;
}

public List<long> eqrr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	//$"{before[commands[0]]}".Dump();
	result[commands[2]] = before[commands[0]] == before[commands[1]] ? 1 : 0;
	return result;
}

public List<long> addr(List<int> commands, List<long> before)
{
	List<long> result = before.ConvertAll(x => x);
	//$"{before[commands[0]]} + {before[commands[1]]}".Dump();
	//$"{before[commands[0]] + before[commands[1]]}".Dump();
	result[commands[2]] = before[commands[0]] + before[commands[1]];
	return result;
}
<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day19.input";
	string[] ogdata = File.ReadAllText(filePath).Split('\n');
	Dictionary<int, (string, List<int>)> commands = new Dictionary<int, (string, List<int>)>();
	int ind = 0;
	foreach (string line in ogdata.ToList().GetRange(1, ogdata.Length-1))
	{
		List<string> splitLine = line.Split(' ', 2).ToList();
		commands.Add(ind, (splitLine[0], splitLine[1].Split(' ').ToList().ConvertAll(x => Int32.Parse(x))));
		ind++;
	}
	//commands.Dump();
	Console.WriteLine($"Part one: {part1(ogdata[0].Trim(), commands)}");
	Console.WriteLine($"Part two: {part2(ogdata[0].Trim(), commands)}"); // super cheated off of Peter here, turns out this is trying to find the sum of the factors of a large number, so I just did that in python command line
}

// You can define other methods, fields, classes and namespaces here
public int part1(string ipData, Dictionary<int, (string, List<int>)> program)
{
	int ip = 0;
	int ipIndex = Int32.Parse(ipData.Substring(ipData.LastIndexOf(' ')+1));;
	Dictionary<string, Func<List<int>, List<int>, List<int>>> opcodes = new Dictionary<string, Func<List<int>, List<int>, List<int>>>
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
	List<int> registers = new List<int> { 0, 0, 0, 0, 0, 0 };
	while (ip < program.Count)
	{
		List<int> command = program[ip].Item2;
		registers[ipIndex] = ip;
		registers = opcodes[program[ip].Item1](command, registers);
		ip = registers[ipIndex];
		ip++;
	}
	return registers[0];
}

public int part2(string ipData, Dictionary<int, (string, List<int>)> program)
{
	int ip = 0;
	int ipIndex = Int32.Parse(ipData.Substring(ipData.LastIndexOf(' ') + 1)); ;
	Dictionary<string, Func<List<int>, List<int>, List<int>>> opcodes = new Dictionary<string, Func<List<int>, List<int>, List<int>>>
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
	List<int> registers = new List<int> { 1, 0, 0, 0, 0, 0 };
	while (ip < program.Count)
	{
		List<int> command = program[ip].Item2;
		registers[ipIndex] = ip;
		registers = opcodes[program[ip].Item1](command, registers);
		ip = registers[ipIndex];
		ip++;
	}
	return registers[0];
}

public List<int> addi(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);  //quick 'n' easy deep copy
	result[commands[2]] = before[commands[0]] + commands[1];
	return result;
}

public List<int> mulr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] * before[commands[1]];
	return result;
}

public List<int> muli(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] * commands[1];
	return result;
}

public List<int> banr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] & before[commands[1]];
	return result;
}

public List<int> bani(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] & commands[1];
	return result;
}

public List<int> borr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] | before[commands[1]];
	return result;
}

public List<int> bori(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] | commands[1];
	return result;
}

public List<int> setr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]];
	return result;
}

public List<int> seti(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = commands[0];
	return result;
}

public List<int> gtir(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = commands[0] > before[commands[1]] ? 1 : 0;
	return result;
}

public List<int> gtri(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] > commands[1] ? 1 : 0;
	return result;
}

public List<int> gtrr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] > before[commands[1]] ? 1 : 0;
	return result;
}

public List<int> eqir(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = commands[0] == before[commands[1]] ? 1 : 0;
	return result;
}

public List<int> eqri(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] == commands[1] ? 1 : 0;
	return result;
}

public List<int> eqrr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] == before[commands[1]] ? 1 : 0;
	return result;
}

public List<int> addr(List<int> commands, List<int> before)
{
	List<int> result = before.ConvertAll(x => x);
	result[commands[2]] = before[commands[0]] + before[commands[1]];
	return result;
}
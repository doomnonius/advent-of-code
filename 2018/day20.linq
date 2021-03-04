<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day20.testinput";
	string ogdata = File.ReadAllText(filePath).Trim();
	//ogdata.Dump();
	Console.WriteLine($"Part one: {part1(ogdata.ToCharArray().Skip(1).Take(ogdata.Length-2).ToArray()).Item1}");
	//Console.WriteLine($"Part two: {part2()}");
}

// You can define other methods, fields, classes and namespaces here
public (int, int) part1(char[] input)
{
	int retVal = 0;
	List<int> alts = new List<int> {};
	for (int i = 0; i < input.Length; i++)
	{
		char c = input[i];
		c.Dump();
		if (c == '(')
		{
			//Console.WriteLine("Next layer from open");
			(int n, int j) = part1(input.Skip(i+1).Take(input.Length - (i + 1)).ToArray());
			retVal += n;
			i += j;
			Console.WriteLine($"We are now at index: {i}");
			//retVal.Dump();
		}
		else if (c == '|')
		{
			//Console.WriteLine("Next layer from or");
			(int n, int j) = part1(input.Skip(i+1).Take(input.Length - (i + 1)).ToArray());
			alts.Add(n);
			i += j;
			Console.WriteLine($"We are now at index: {i}");
			//alts.Dump();
		}
		else if (c ==')')
		{
			int m = 0;
			if (alts.Contains(0))
			{
				return (0, i + 1);
			}
			else
			{
				try
				{
					m = alts.Max();
				}
				catch { }
				return m > retVal ? (m, i) : (retVal, i);
			}
		}
		else
		{
			retVal++;
		}
	}
	return (retVal, 0);
}
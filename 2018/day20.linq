<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day20.input";
	string ogdata = File.ReadAllText(filePath).Trim();
	ogdata.Length.Dump();
	Console.WriteLine($"Part two: {part2b(ogdata.ToCharArray().Skip(1).Take(ogdata.Length-2).ToArray())}"); // not 10057, too high; 9031 also too high; 8109 too low; nor 84??; not 8201; not 8277; correct is 8186, but not there yet
	// figure out where/how these two diverge 2b is correct (at least partially)
}

// You can define other methods, fields, classes and namespaces here
public int part2b(char[] input)
{
	int retVal = 0;
	List<int> findMax = new List<int>();
	foreach (int i in part1c(input))
	{
		findMax.Add(i);
		if (i >= 1000)
		{
			//i.Dump();
			retVal++;
		}
		else if (i < 0) retVal += i;
	}
	Console.WriteLine($"Part one: {findMax.Max()}");
	//Console.WriteLine($"Part two: {findMax.Where(t => t >= 1000).Count()}");
	return retVal;
}

public static System.Collections.Generic.IEnumerable<int> part1c(char[] input)
{
	Dictionary<int, int> opens = new Dictionary<int, int>();
	int retVal = 1;
	for (int i = 0; i < input.Length; i++)
	{
		char c = input[i];
		if (c == '(')
		{
			opens.Add(i, retVal);
			continue;
		}
		else if (c == '|')
		{
			retVal = opens.Last().Value;
			continue;
		}
		else if (c == ')')
		{
			KeyValuePair<int, int> last = opens.Last();
			opens.Remove(last.Key);
			continue;
		}
		if (/*retVal == 1000 || */ i < 200)
		{
			//(i, retVal).Dump();
		}
		yield return retVal;
		retVal++;
	}
}
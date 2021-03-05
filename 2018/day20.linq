<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day20.testinput";
	string ogdata = File.ReadAllText(filePath).Trim();
	ogdata.Length.Dump();
	Console.WriteLine($"Part one: {part1(ogdata.ToCharArray().Skip(1).Take(ogdata.Length-2).ToArray()).Item1}"); // not 1503, too low
	Console.WriteLine($"Part two: {part2(ogdata.ToCharArray().Skip(1).Take(ogdata.Length-2).ToArray())}"); // not 10057, too high; 9031 also too high; 8109 too low; nor 84??; 
}

// You can define other methods, fields, classes and namespaces here
public int part2(char[] input)
{
	int retVal = 0;
	for (int i = 0; i < input.Length; i++) // nothing less than a thousand characters could possibly be 1000 doors away... I thought
	{
		if (input[i] == ')' || input[i] == '(' || input[i] == '|') continue;
		char[] sub = input.Take(i+1).ToArray();
		int open = sub.Where(x => x == '(').Count();
		int close = sub.Where(x => x == ')').Count();
		for (int j = 0; j < open-close; j++) sub = sub.Append(')').ToArray();
		List<int> ret;
		int r = part1b(sub, out ret).Item1;
		try
		{
			if (ret.Last().Dump() >= 5)
			{
				retVal++;
			}
		}
		catch {}
	}
	return retVal;
}

public int part2b(char[] input)
{
	int retVal = 0;
	foreach (int i in part1c(input))
	{
		//i.Dump();
		if (i >= 1000)
		{
			retVal++;
		}
		else if (i == -1) retVal--;
	}
	return retVal;
}

public static System.Collections.Generic.IEnumerable<int> part1c(char[] input)
{
	Dictionary<int, int> opens = new Dictionary<int, int>();
	int retVal = 0;
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
			if (last.Value == retVal)
			{
				retVal = last.Value;
			}
			yield return -1;
		}
		retVal++;
		if (retVal >= 1000)
		{
			//(i, retVal).Dump();
		}
		yield return retVal;
	}
}

// this one calculates how many doors away the last item of a subsection is - not super efficient because it starts over from the beginning each time, and kind of has too because it's recursive - also doesn't even return the right answer
public (int, int) part1b(char[] input, out List<int> overK, int lastOpen = 0, int retVal = 0)
{
	List<int> alts = new List<int>();
	overK = new List<int>();
	for (int i = 0; i < input.Length; i++)
	{
		char c = input[i];
		if (c == '(')
		{
			lastOpen = retVal + lastOpen;
			(int n, int j) = part1b(input.Skip(i + 1).Take(input.Length - (i + 1)).ToArray(), out overK, lastOpen);
			retVal = n + lastOpen;
			i += j + 1; // + 1 here because each ')' needs to close once for each '|' and each '(' before it, and when it closes for '(' it needs to move one, but not when it closes for a '|'
		}
		else if (c == '|')
		{
			(int n, int j) = part1b(input.Skip(i + 1).Take(input.Length - (i + 1)).ToArray(), out overK, lastOpen);
			alts.Add(lastOpen + retVal);
			i += j;
		}
		else if (c == ')')
		{
			int m = 0;
			if (alts.Contains(0))
			{
				return (0, i);
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
			overK.Add(retVal + lastOpen);
		}
	}
	return (retVal, 0);
}

public (int, int) part1(char[] input)
{
	int retVal = 0;
	List<int> alts = new List<int> {};
	for (int i = 0; i < input.Length; i++)
	{
		char c = input[i];
		if (c == '(')
		{
			(int n, int j) = part1(input.Skip(i+1).Take(input.Length - (i + 1)).ToArray());
			retVal += n;
			i += j + 1; // + 1 here because each ')' needs to close once for each '|' and each '(' before it, and when it closes for '(' it needs to move one, but not when it closes for a '|'
		}
		else if (c == '|')
		{
			(int n, int j) = part1(input.Skip(i+1).Take(input.Length - (i + 1)).ToArray());
			alts.Add(n);
			i += j;
		}
		else if (c ==')')
		{
			int m = 0;
			if (alts.Contains(0))
			{
				return (0, i);
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
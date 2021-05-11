<Query Kind="Program">
  <IncludeUncapsulator>false</IncludeUncapsulator>
</Query>

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2017\day16.input";
	List<string> data = File.ReadAllText(filePath).Split(',').ToList();
	List<char> dancers = new List<char>();
	for (char x = 'a'; x <= 'p'; x++)
	{
		dancers.Add(x);
	}
	Console.WriteLine($"Part one: {part1(data, dancers.ConvertAll(x => x))}");
	Console.WriteLine($"Part two: {part2(data, dancers)}");
}

// You can define other methods, fields, classes and namespaces here
public List<char> part2(List<string> inp, List<char> dancers)
{
	int retVal = 0;
	
	
	return dancers;
}

public List<char> part1(List<string> inp, List<char> dancers)
{
	foreach (string inst in inp)
	{
		if (inst.StartsWith("s"))
		{
			int n = Int32.Parse(inst.Substring(1));
			int m  = dancers.Count() - n
			List<char> p1 = dancers.GetRange(m, n);
			List<char> p2 = dancers.GetRange(0, 16-n);
			dancers = p1;
			dancers.AddRange(p2);
		}
		else if (inst.StartsWith("x"))
		{
			string[] s = inst.Substring(1).Split('/');
			int n1 = Int32.Parse(s[0]);
			int n2 = Int32.Parse(s[1]);
			
		}
		else if (inst.StartsWith("p"))
		{
			string[] s = inst.Substring(1).Split('/');
		}
	}



	return dancers;
}
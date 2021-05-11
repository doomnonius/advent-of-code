<Query Kind="Program">
  <Namespace>System.IO</Namespace>
</Query>

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day01.input";
	List<string> data = File.ReadAllText(filePath).Split('\n').ToList();

	Console.WriteLine($"Part one: {data.Sum(x => Convert.ToInt64(x))}");
	Console.WriteLine($"Part two: {findRepeat(data.ConvertAll(Convert.ToInt32))}");
}

// Define other methods and classes here
public int findRepeat(List<int> data)
{
	int sum = 0;
	List<int> seen = new List<int>();
	while (true)
	{
		foreach (int num in data)
		{
			sum = sum + num;
			//Console.WriteLine(seen);
			if (seen.Contains(sum))
			{
				return sum;
			}
			else
			{
				seen.Add(sum);
			}
		}
	}
}
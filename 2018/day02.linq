<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day02.input";
	List<string> data = File.ReadAllText(filePath).Split('\n').ToList();

	Console.WriteLine($"Part one: {part1(data)}");
	Console.WriteLine($"Part two: {part2(data)}");
}
public string part2 (List<string> data)
{
	foreach (string barcode in data)
	{
		foreach (string barcode2 in data)
		{
			if (barcode != barcode2)
			{
				List<char> bList = barcode.ToList();
				List<char> bList2 = barcode2.ToList();
				int i = 0;
				int diffs = 0;
				while (i < bList.Count && diffs < 2)
				{
					if (bList[i] != bList2[i])
					{
						diffs++;
					}
					i++;
				}
				if (diffs == 1)
				{
					Console.WriteLine(barcode);
					Console.WriteLine(barcode2);
				}
			}
		}
	}
	return "Done!";
}

public int part1 (List<string> data)
{
	int twoCount = 0;
	int threeCount = 0;
	
	foreach (string barcode in data)
	{
		bool twoHit = true;
		bool threeHit = true;
		foreach (char c in barcode)
		{
			int count = barcode.Count(f => f == c);
			if (count == 2 && twoHit)
			{
				twoCount++;
				twoHit = false;
			}
			else if (count == 3 && threeHit)
			{
				threeCount++;
				threeHit = false;
			}
		}
	}
	return twoCount * threeCount;
}
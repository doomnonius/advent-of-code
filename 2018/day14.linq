<Query Kind="Program" />

void Main()
{
	List<int> scores = "37".ToList().ConvertAll(x => x.ToString()).ConvertAll(x => Int32.Parse(x));
	Console.WriteLine($"Part one: {part1(scores, 5, 10)}"); // not 1076555555, too high; not 1021124482, too low; interpreted directions incorrectly
	List<byte> nums = "37".ToList().ConvertAll(x => x.ToString()).ConvertAll(x => Byte.Parse(x));
	Console.WriteLine($"Part two: {part2(nums, "824501")}"); // wasn't properly checking for match initially
}

// You can define other methods, fields, classes and namespaces here
public int part1 (List<int> recipes, int start_at, int result_length)
{
	int initial_length = recipes.Count;
	int final_length = start_at + result_length;
	int elf1 = 0;
	int elf2 = 1;
	while (recipes.Count < final_length)
	{
		int new_scores = recipes[elf1] + recipes[elf2];
		if (new_scores > 9)
		{
			recipes.Add(1);
		}
		recipes.Add(new_scores % 10);
		elf1 = (elf1 + 1 + recipes[elf1]) % recipes.Count;
		elf2 = (elf2 + 1 + recipes[elf2]) % recipes.Count;
	}
	int retVal = 0;
	foreach (int x in recipes.GetRange(start_at, result_length))
	{
		retVal = 10 * retVal + x;
	}
	return retVal;
}

public int part2(List<byte> recipes, string match_pat)
{
	List<byte> patt = match_pat.ToList().ConvertAll(x => x.ToString()).ConvertAll(x => Byte.Parse(x));
	int result_length = patt.Count;
	int elf1 = 0;
	int elf2 = 1;
	int i = 0;
	int count = recipes.Count;
	while (true) 
	{
		byte new_scores = (byte)(recipes[elf1] + recipes[elf2]);
		if (new_scores > 9)
		{
			recipes.Add(1);
			count++;
			if (count > result_length && checkMatch(recipes.GetRange(count - result_length, result_length), patt))
			{
				return count - result_length;
			}
			recipes.Add((byte)(new_scores-10));
			count++;
		}
		else
		{
			recipes.Add(new_scores);
			count++;
		}
		if (count > result_length && recipes.Last() == patt.Last())
		{
			if (checkMatch(recipes.GetRange(count - result_length, result_length), patt))
			{
				return count - result_length;
			}
		}
		int next_elf1 = (elf1 + 1 + recipes[elf1]);
		int next_elf2 = (elf2 + 1 + recipes[elf2]);
		elf1 = next_elf1 % count;
		elf2 = next_elf2 % count;
		i++;
	}
}

public bool checkMatch (List<byte> result, List<byte> patt)
{
	bool retVal = true;
	for (int x = result.Count-1; x >= 0; x--)
	{
		if (result[x] != patt[x])
		{
			retVal = false;
			break;
		}
	}
	return retVal;
}
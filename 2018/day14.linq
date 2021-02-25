<Query Kind="Program" />

void Main()
{
	List<int> scores = "37".ToList().ConvertAll(x => x.ToString()).ConvertAll(x => Int32.Parse(x));
	scores.Dump();
	Console.WriteLine($"Part one: {part1(scores, 10)}"); // not 1076555555, too high; not 1021124482, too low; 
	//Console.WriteLine($"Part two: {part2()}")
}

// You can define other methods, fields, classes and namespaces here
public int part1 (List<int> recipes, int result_length)
{
	int initial_length = recipes.Count;
	int final_length = initial_length + result_length;
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
	foreach (int x in recipes.GetRange(initial_length, result_length))
	{
		retVal = 10 * retVal + x;
	}
	return retVal;
}
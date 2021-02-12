<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day06.input";
	List<char> data = File.ReadAllText(filePath).ToList();
	Console.WriteLine($"Part one: {part1(data)}");
	//Console.WriteLine($"Part two: {part2(data)}");
}

// Define other methods and classes here

<Query Kind="Program">
  <IncludeUncapsulator>false</IncludeUncapsulator>
</Query>

void Main()
{
	int DATA_A = 512;
	int DATA_B = 191;
	//Console.WriteLine($"Part one: {part1(DATA_A, DATA_B)}");
	Console.WriteLine($"Part two: {part2(DATA_A, DATA_B)}");
}

// You can define other methods, fields, classes and namespaces here
public int part2 (long valueA, long valueB)
{
	int retVal = 0;
	int factorA = 16807;
	int factorB = 48271;
	int mod = 2147483647;
	int bits16 = 65536;
	for (int i = 0; i < 5000000; i++)
	{
		while (true)
		{
			valueA = (valueA * factorA);
			if (valueA > mod) valueA = valueA % mod;
			if (valueA % 4 == 0) break;
		}
		while (true)
		{
			valueB = (valueB * factorB);
			if (valueB > mod) valueB = valueB % mod;
			if (valueB % 8 == 0) break;
		}
		if (valueA % bits16 == valueB % bits16)
		{
			retVal++;
		}
	}
	return retVal;
}

public int part1 (long valueA, long valueB)
{
	int retVal = 0;
	int factorA = 16807;
	int factorB = 48271;
	int mod = 2147483647;
	int bits16 = 65536;
	for (int i = 0; i < 40000000; i++)
	{
		valueA = (valueA * factorA);
		if (valueA > mod) valueA = valueA % mod;
		valueB = (valueB * factorB);
		if (valueB > mod) valueB = valueB % mod;
		if (valueA % bits16 == valueB % bits16)
		{
			retVal++;
		}
	}
	return retVal;
}
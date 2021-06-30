<Query Kind="Program" />

void Main()
{
	//for (long i = 10626258; i <= 12361563; i++)
	//{
		//List<long> regs = new List<long> {1, 0, 0, 0, 0, 0};
	List<long> seen = new List<long> ();
	bool p1 = true;
	bool broken = false;
	long r5 = 0;
	long r4 = 0;
	long r2 = 0;
	long r1 = 0;
	bool skipped = true;
	while (true)
	{
		if (r4 > 0)
		{
			if (p1)
			{
				Console.WriteLine($"Part one: {r4}");
				p1 = false;
			}
			if (seen.Contains(r4))
			{
				Console.WriteLine($"Part two: {seen.Last()}");
				return;
			}
			else
			{
				seen.Add(r4);
			}
		}
		//r4.Dump();
		//seen.Dump();
		//r0.Dump();
		r1 = r4 | 65536;
		r4 = 678134;
		while (true)
		{
			r5 = r1 & 255;
			r4 = r4 + r5;
			r4 = r4 & 16777215;
			r4 = r4 * 65899;
			r4 = r4 & 16777215;
			if (256 > r1)
			{
				break;
			}
			r5 = 0;
			while (true)
			{
				r2 = r5 + 1;
				r2 *= 256;
				if (r2 > r1)
				{
					r1 = r5;
					break;
				}
				r5++;
			}
		}
	}
}

// You can define other methods, fields, classes and namespaces here

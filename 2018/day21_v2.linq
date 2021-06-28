<Query Kind="Program" />

void Main()
{
	//List<long> regs = new List<long> {1, 0, 0, 0, 0, 0};
	long r5 = 0;
	long r4 = -1;
	long r3 = 0;
	long r2 = 0;
	long r1 = 0;
	long r0 = 2000000000;
	bool skipped = true;
	while (r4 != r0)
	{
		r4.Dump();
		r1.Dump();
		if (skipped)
		{
			r4 = 0;
			r1 = r4 | 65536;
			r4 = 678134;
		}
		skipped = true;
		r5 = r1 & 255;
		r4 = r4 + r5;
		r4 = r4 & 16777215;
		r4 = r4 * 65899;
		r4 = r4 & 16777215;
		while (r1 > 255)
		{
			//r1.Dump();
			r5 = 0;
			r2 = 256;
			//r2 = r5 + 1;
			//r2 = r2 * 256;
			while (r2 < r1)
			{
				r5++;
				r2 += 256;
				//r2 = r5 + 1;
				//r2 = r2 * 256;
			}
			r1 = r5;
			skipped = false;
			break;
		}
	}
	"Finished!".Dump();
}

// You can define other methods, fields, classes and namespaces here

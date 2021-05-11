<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day04.input";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	List<string> stuff = ogdata.Select(t => t).OrderBy(t => DateTime.Parse(t.Substring(1, t.IndexOf("]")-1))).ToList();
	//stuff[0].Dump();
	List<Timestamp> times = new List<Timestamp> ();
	int last_id = 0;
	foreach (string t in stuff)
	{
		int id = t.Contains("#") ? Int32.Parse(t.Substring(t.IndexOf("#") + 1, t.IndexOf("b") - 2 - t.IndexOf("#"))) : last_id;
		last_id = id;
		times.Add(new Timestamp
			{
				time = DateTime.Parse(t.Substring(1, t.IndexOf("]")-1)),
				id = last_id,
				action =  t.Contains("#") ? t.Substring(t.IndexOf("b")) : t.Substring(t.IndexOf("]")+2)
			}
		);
	}
	//times.Dump();
	Console.WriteLine($"Part one: {part1(times)}"); // not 3443, too low
	//Console.WriteLine($"Part two: {part2(data)}");
}

// Define other methods and classes here
public int part1 (List<Timestamp> events)
{
	Dictionary<int, List<DateTime>> sleepTimes = new Dictionary<int, List<DateTime>> ();
	foreach (Timestamp e in events)
	{
		if (e.action.StartsWith("b")) {
			continue;
		}
		if (sleepTimes.ContainsKey(e.id)) {
			sleepTimes[e.id].Add(e.time);
		}
		else
		{
			sleepTimes.Add(e.id, new List<DateTime> ());
			sleepTimes[e.id].Add(e.time);
		}
	}
	//sleepTimes[313].Dump();
	List<int> t = sleepTimes.Keys.ToList();
	Dictionary<int, int> totalSleep = new Dictionary<int, int> ();
	Dictionary<int, Dictionary<int,int>> minutesAsleep = new Dictionary<int, Dictionary<int,int>>();
	foreach (int id in t)
	{
		totalSleep.Add(id, 0);
		for (int i = 0; i < sleepTimes[id].Count; i += 2)
		{
			int later = sleepTimes[id][i + 1].Minute;
			int earlier = sleepTimes[id][i].Minute;
			totalSleep[id] += later - earlier;
			if (!minutesAsleep.ContainsKey(id)) minutesAsleep.Add(id, new Dictionary<int, int>());
			for (int j = earlier; j < later; j++)
			{
				if (minutesAsleep[id].ContainsKey(j)) {
					minutesAsleep[id][j]++;
				} else {
					minutesAsleep[id].Add(j, 1);
				}
			}
		}
	}
	int a = totalSleep.Where(s => s.Value == totalSleep.Values.Max()).Select(z => z.Key).First();
	//totalSleep.Dump("Total sleep");
	int b = minutesAsleep[a].Where(s => s.Value == minutesAsleep[a].Values.Max()).Select(z => z.Key).First();
	minutesAsleep.Dump(); // definitely just manually picked part2's answer out from here
	return a * b;
}


public class Timestamp
{
	public DateTime time { get; set; }
	public int id { get; set; }
	public string action { get; set; }
}
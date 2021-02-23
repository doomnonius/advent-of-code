<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day07.input";
	string alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	List<string> ogdata = File.ReadAllText(filePath).Split('\n').ToList();
	List<Rule> rules = new List<Rule>();
	foreach (string line in ogdata)
	{
		string rule = line.Substring(36, 1);
		string pre = line.Substring(5, 1);
		if (rules.Select(r => r.name).Contains(rule))
		{
			List<Rule> z = rules.Where(r => r.name == rule).Take(1).ToList();
			z[0].addPrereq(pre);
		}
		else
		{
			rules.Add(new Rule
				{
					name = rule,
					prereqs = new List<string> { pre },
					time = 60 + alphabet.IndexOf(rule),
					active = false
				}
			);
		}
		if (!rules.Select(r => r.name).Contains(pre))
		{
			rules.Add(new Rule
				{
					name = pre,
					prereqs = new List<string> (),
					time = 60 + alphabet.IndexOf(pre),
					active = false
				}
			);
		}
	}
	//rules.OrderBy(r => r.name).Dump();
	Console.WriteLine($"Part one: {part1(rules)}");
	// I was too lazy to figure out how to do a deep copy
	List<Rule> rules2 = new List<Rule>();
	foreach (string line in ogdata)
	{
		string rule = line.Substring(36, 1);
		string pre = line.Substring(5, 1);
		if (rules2.Select(r => r.name).Contains(rule))
		{
			List<Rule> z = rules2.Where(r => r.name == rule).Take(1).ToList();
			z[0].addPrereq(pre);
		}
		else
		{
			rules2.Add(new Rule
			{
				name = rule,
				prereqs = new List<string> { pre },
				time = 60 + alphabet.IndexOf(rule),
				active = false
			}
			);
		}
		if (!rules2.Select(r => r.name).Contains(pre))
		{
			rules2.Add(new Rule
			{
				name = pre,
				prereqs = new List<string>(),
				time = 60 + alphabet.IndexOf(pre),
				active = false
			}
			);
		}
	}
	Console.WriteLine($"Part two: {part2(rules2)}"); // not 868, too low; 
}

// Define other methods and classes here
public string part1 (List<Rule> rules)
{
	string retVal = "";
	while (rules.Sum(r => r.prereqs.Count) > 0)
	{
		List<Rule> available = rules.Where(r => r.prereqs.Count == 0).OrderBy(r => r.name).ToList();
		//available.Dump();
		string removed = available[0].name;
		retVal = String.Concat(retVal, removed);
		rules.Remove(available[0]);
		foreach (Rule rule in rules)
		{
			if (rule.prereqs.Contains(removed))
			{
				rule.prereqs.Remove(removed);
			}
		}
	}
	
	return retVal;
}

public int part2 (List<Rule> rules)
{
	int retVal = 1;
	Dictionary<int, Rule> workers = new Dictionary<int, Rule>();
	workers.Add(1, new Rule {name = "ph", prereqs = new List<string>(), time = 0, active = false});
	workers.Add(2, new Rule {name = "ph1", prereqs = new List<string>(), time = 0, active = false});
	workers.Add(3, new Rule {name = "ph2", prereqs = new List<string>(), time = 0, active = false});
	workers.Add(4, new Rule {name = "ph3", prereqs = new List<string>(), time = 0, active = false});
	workers.Add(5, new Rule {name = "ph4", prereqs = new List<string>(), time = 0, active = false});
	
	while (rules.Sum(r => r.prereqs.Count) > 0)
	{
		List<Rule> available = rules.Where(r => r.prereqs.Count == 0).OrderBy(r => r.name).ToList();
		//string removed = available[0].name;
		//rules.Remove(available[0]);
		//available.Dump();
		int i = 0;
		foreach (int worker in new List<int> { 1, 2, 3, 4, 5 })
		{
			if (workers[worker].time <= 0 && i < available.Count)
			{
				if (available[i].active == false)
				{
					workers[worker] = available[i];
					available[i].active = true;
				}
				i++;
			}
		}
		foreach (Rule r in workers.Values)
		{
			r.time--;
			if (r.time == 0)
			{
				rules.Remove(r);
				foreach (Rule rule in rules)
				{
					if (rule.prereqs.Contains(r.name))
					{
						rule.prereqs.Remove(r.name);
					}
				}
			}
		}
		retVal++;
		if (retVal%100 == 0)
		{
			//retVal.Dump();
			//rules.OrderBy(r => r.name).Dump();
		}
		//workers.Dump();
	}
	return retVal;
}

public class Rule
{
	public string name { get; set; }
	public List<string> prereqs { get; set; }
	public int time { get; set; }
	public bool active { get; set; }
	
	public void addPrereq (string p)
	{
		this.prereqs.Add(p);
	}
}
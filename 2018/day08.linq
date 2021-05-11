<Query Kind="Program" />

void Main()
{
	string filePath = @"C:\projects\python\advent-of-code\2018\day08.input";
	List<string> ogdata = File.ReadAllText(filePath).Split().ToList();
	List<int> data = ogdata.ConvertAll(a => Int32.Parse(a));
	Console.WriteLine($"Part one: {sumMetadata(createNodes(data))}");
	Console.WriteLine($"Part one: {nodeValue(createNodes(data)[0])}");
}

// Define other methods and classes here
public List<Node> createNodes (List<int> data)
{
	int i = 0;
	List<Node> c = new List<Node> ();
	while (i < data.Count)
	{
		c.Add(createNode(data.GetRange(i, data.Count - i)));
		i = c.Sum(x => measureNode(x));
	}
	return c;
}

public Node createNode(List<int> data)
{
	List<Node> c = new List<Node> ();
	int child_count = 0;
	int start = 2;
	while (child_count < data[0] && data.Count > 1)
	{
		c.Add(createNode(data.GetRange(start, data.Count - start)));
		child_count++;
		start += measureNode(c.Last());
	}
	return new Node {
		num_children = data[0],
		num_meta = data[1],
		children = c,
		metadata = data.GetRange(c.Sum(x => measureNode(x))+2, data[1])
	};
}

public int measureNode(Node n)
{
	int retVal = 2 + n.metadata.Count;
	foreach (Node c in n.children)
	{
		retVal += measureNode(c);
	}
	return retVal;
}

public int sumMetadata(List<Node> ns)
{
	int retVal = 0;
	foreach (Node n in ns)
	{
		retVal += n.metadata.Sum();
		retVal += sumMetadata(n.children);
	}
	return retVal;
}

public int nodeValue (Node n)
{
	int retVal = 0;
	if (n.children.Count > 0)
	{
		foreach (int x in n.metadata)
		{
			if (x > 0 && x <= n.children.Count)
			{
				retVal += nodeValue(n.children[x-1]);
			}
		}
	}
	else
	{
		retVal += n.metadata.Sum();
	}
	return retVal;
}

public class Node
{
	public int num_children { get; set; }
	public int num_meta { get; set; }
	public List<Node> children { get; set; }
	public List<int> metadata { get; set; }
}
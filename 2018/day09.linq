<Query Kind="Program" />

void Main()
{
	string input = "447 players; last marble is worth 71510 points";
	Console.WriteLine($"Part one: {part1(447, 71510)}");
	Console.WriteLine($"Part two: {part1(447, 7151000)}"); // just brute forcing it; 23:15
}

// Define other methods and classes here
public long part1 (int players, int last_marble)
{
	List<int> circle = new List<int> { 0 };
	Dictionary<int, long> scores = new Dictionary<int, long> ();
	int curr_marble = 0;
	int marble_count = 1;
	int curr_player = 1;
	int circle_length = 1;
	while (marble_count <= last_marble)
	{
		int next = (curr_marble + 1) % circle_length;
		int next_next = (curr_marble + 2) % circle_length;
		if (circle_length == 1)
		{
			circle.Add(1);
			curr_marble = 1;
			circle_length++;
		}
		else
		{
			if (marble_count % 23 == 0)
			{
				if (!scores.Keys.Contains(curr_player))
				{
					scores.Add(curr_player, 0);
				}
				scores[curr_player] += marble_count;
				int removal = (((curr_marble - 7) % circle_length) + circle_length) % circle_length;
				//removal.Dump();
				scores[curr_player] += circle[removal];
				circle.RemoveAt(removal);
				curr_marble = removal;
				circle_length--;
			}
			else
			{
				circle.Insert(next_next, marble_count);
				curr_marble = next_next;
				circle_length++;
			}
		}
		//circle.Dump();
		marble_count++;
		curr_player = curr_player % players + 1;
	}
	return scores.Max(x => x.Value);
}
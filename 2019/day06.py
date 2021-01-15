class Planet:
	def __init__(self, planet, moon):
		self.name = planet
		self.orbited = moon

new_inp = inp.split(",")
dict_inp = dict()
for key, value in [new_inp[x].split(")") for x in range(len(new_inp))]:
	if key in dict_inp:
		dict_inp[key].append(value)
	else:
		dict_inp[key] = [value]


def populate(D):
	
	def sub_pop(D, galaxy = None, initial = "COM"):
		if galaxy == None:
			galaxy = Tree()
			galaxy.create_node(initial, initial)
		for x in D[initial]:
			galaxy.create_node(x, x, initial)
			if x in D:
				sub_pop(D, galaxy, x)
		return galaxy
	
			
	galactic = sub_pop(D)
	return galactic

# def galaxy_builder(inp, left = [range(len(inp))], galaxy=None):
#     if galaxy == None:
#         galaxy = Tree()
#         galaxy.create_node("COM", "COM")
#     x = 0
#     loose = []
#     for x in left:
#         print(x)
#         parent, child = inp[x].split(")")
#         # if the parent is not in the tree yet, push it to the end of the list
#         if galaxy.contains(parent): # if parent does exist, create child node
#             galaxy.create_node(child, child, parent=parent)
#         else: # push to end of list; not efficient
#             loose.append(x)
#         x += 1
#     if loose == []:
#         return galaxy
#     else:
#         galaxy_builder(inp, left=loose, galaxy=galaxy)
#     return galaxy
		
""" Idea: go from one end of list, create a second list with the pointers that couldn't be place, then go through that list, which will create a new list, etc.
"""
answer = populate(dict_inp)

orbits = 0
for x in answer.nodes:
	orbits += answer.depth(x)
print(orbits)
has = []
for x in answer.nodes:
	if answer.is_ancestor(x, "YOU") and answer.is_ancestor(x, "SAN"):
		has.append((x, answer.depth(x)))
has.sort(key=lambda x: x[1], reverse=True)
sub = answer.subtree(has[0][0])
final = sub.depth("YOU") + sub.depth("SAN") - 2
print(final)


if __name__ == "__main__":
	import os, timeit
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(os.path.join(FILE_DIR, "day06.input")) as f:
		DATA = f.read().strip()
	DATA = [x.split(")") for x in DATA.split("\n")]
	print(f"Part one: {DATA}")
	# print(f"Part two: {}")
	# print(f"Time: {timeit.timeit('', setup='from __main__ import ', number = 1)}")
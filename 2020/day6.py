def all_yes(form):
	"""Returns the number of questions that all members of a group answered yes to.
	"""
	return len({char for char in set(form) if form.count(char) == (form.count("\n") + 1)})

if __name__ == "__main__":
	import os
	FILE_DIR = os.path.dirname(os.path.abspath(__file__))
	with open(FILE_DIR + "\\day6.input") as f:
		DATA = f.read().strip()
	FORMS = DATA.split("\n\n")
	# print(sum(all_yes(a) for a in FORMS)) # old solution
	print(sum(all_yes(form) for form in FORMS)) # "simplified" solution
import argparse
argparse = argparse.ArgumentParser()
argparse.add_argument("file")
args = argparse.parse_args()

with open(args.file) as data_file, open("cuvinte_wordle.txt") as db_file:
	data = [x.split() for x in data_file.readlines() if not x.startswith("#")]
	words = db_file.read().split()
	avg_g = sum([len(x) - 1 for x in data])/len(data)
	print(f"Average guesses: {avg_g}")
	over_6 = sum([1 if len(line) > (6 + 1) else 0 for line in data])
	g_dict = dict()
	for x in data:
		y = len(x) - 1
		g_dict[y] = g_dict.get(y, 0) + 1
		if x[0] != x[-1]:
			print(f"Invalid line {x}!")
		for i in x:
			if i not in words:
				print(f"Invalid word {i}!")
	g_list = [x[1] for x in sorted(g_dict.items())]
	for i, x in enumerate(g_list):
		print(f"Words with {i + 1} guesses: {x} ({x / len(data) * 100}%)")
	print(f"Words with over 6 guesses: {over_6} ({over_6 / len(data) * 100}%)")
	s_data = {x[0] for x in data}
	if len(s_data) == len(words) == len(data):
		print("Lengths matchings.")
	else: print("Lengths do not match!")

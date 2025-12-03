#################################################################
###### https://adventofcode.com/2024/day/3 #######################
#################################################################

file = "input.txt"

DAY_NO = "3"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]

total = 0
for bank in cleanInput:
	# need to find largest
	largest = 0
	secondLargest = 0
	largestCellIndex = 0
	set = 0
	for celIndex, cell in enumerate(bank):
		if set and (int(cell) > secondLargest):
			secondLargest = int(cell)
		if (int(cell) > largest) and (celIndex != (len(bank) - 1)):
			largest = int(cell)
			secondLargest = 0
			set = 1

	num = int(f"{largest}{secondLargest}")
	total += num

print(total)
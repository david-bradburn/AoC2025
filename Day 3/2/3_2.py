#################################################################
###### https://adventofcode.com/2024/day/3 #######################
#################################################################

file = "input.txt"

DAY_NO = "3"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]

total = 0

def findMax(start:int, stop:int, line:list):
	slice = line[start: stop+1]
	maxVal = max(slice)
	indexMaxVal = slice.index(maxVal)
	return maxVal, indexMaxVal+ start + 1

for bank in cleanInput:
	# need to find largest
	numbersNeed = 12

	bankLen = len(bank)
	assert(bankLen > numbersNeed)
	bankarr = [cell for cell in bank]
	testindex = 0
	value = ""
	for pos in range(numbersNeed):
		tmpVal, testindex = findMax(testindex, bankLen - 1 - (11 - pos), bank)
		value += tmpVal


	print(f"{value}")
	total += int(value)

print(total)
#################################################################
###### https://adventofcode.com/2024/day/6 ######################
#################################################################
import re
# misc functions
def fprint(debug: str) -> str:
	print(debug)
	return debug + "\n"

def debugLog(debugString: str):
	fileLoc = ".\Day" + DAY_NO +"\misc\zdebug.txt"
	with open(fileLoc, "w") as fd:
		fd.writelines(debugString)

file = "input.txt"

DAY_NO = "6"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]

hasSpaces = []
for line in cleanInput:
	hasSpaces.append(re.split(r'\s+',line))

data = []
for line in hasSpaces:
	tmpArr = []
	for entry in line:
		if entry == "":
			continue
		else:
			tmpArr.append(entry)
	data.append(tmpArr)

for line in data:
	assert(len(line) == len(data[0]))
print(data)


inputNumbers = []

for lineIndex, line in enumerate(data):
	for entryindex, entry in enumerate(line):
		if lineIndex == 0:
			inputNumbers.append([int(entry)])
		else:
			try:
				a = int(entry)
				inputNumbers[entryindex].append(int(entry))
			except:
				inputNumbers[entryindex].append(str(entry))

print(inputNumbers)
total = 0

for podQuestion in inputNumbers:
	op = podQuestion[-1]

	result = 0
	match op:

		case "+":
			for i in podQuestion[:-1]:
				result+= i

		case "*":
			result  = 1
			for i in podQuestion[:-1]:
				result*=i

	total += result

print(total)

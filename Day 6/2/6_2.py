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
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

rawInput = [n.strip("\n") for n in rawInput]

# hasSpaces = []
longestline = 0
for line in rawInput:
	if len(line) > longestline:
		longestline = len(line)

for lineIndex, line in enumerate(rawInput):
	if len(line) < longestline:
		for i in range(longestline - len(line)):
			rawInput[lineIndex]+=" "

print(rawInput)

for line in rawInput:
	assert(len(line) == len(rawInput[0]))

coulmnHeightMax = len(rawInput) - 1
print(f"Equation Height: {coulmnHeightMax}")

comstr = ""


for i in range(coulmnHeightMax):
	comstr += " "

equationIndex=0

equations = []
for characterIndex in range(len(rawInput[0])):
	columnCount = 0
	tmpstr = ""
	for hIndex in range(len(rawInput) - 1):
		character = rawInput[hIndex][characterIndex]
		tmpstr += character

	if comstr == tmpstr:
		equationIndex += 1
	else:
		try:
			equations[equationIndex].append(int(tmpstr))
		except:
			equations.append([])
			equations[equationIndex].append(int(tmpstr))


print(equations)

ops = rawInput[-1].split()
print(ops)
for opindex, op in enumerate(ops):
	equations[opindex].append(op)


total = 0

for podQuestion in equations:
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

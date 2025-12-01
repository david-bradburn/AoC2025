#################################################################
###### https://adventofcode.com/2024/day/1 #######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [i.strip("\n") for i in rawInput]
print(cleanInput)
movement = [(n[0], int(n[1:])) for n in cleanInput]
print(movement)
startingPos = 50

MAX = 99
MIN = 0

trueCount = 0

curPos = startingPos
for (dir, num) in movement:
	if dir == "L":
		curPos -= num
		if curPos < MIN:
			while (curPos < MIN):
				curPos += 100

	else:
		assert dir == "R"
		curPos += num
		if curPos > MAX:
			curPos -= 100
			while (curPos > MAX):
				curPos -= 100
	print(f"{dir}{num}, {curPos}")

	if (curPos == 0):
		trueCount += 1



print(trueCount)

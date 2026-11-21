#################################################################
###### https://adventofcode.com/2024/day/1 #######################
#################################################################

file = "input.txt"

DAY_NO = "1"
PART = "2"

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
		for n in range(num):
			curPos += 1
			if curPos > MAX:
				curPos = MIN
			if (curPos == 0):
				trueCount += 1
	else:
		assert dir == "R"
		for n in range(num):
			curPos -= 1
			if curPos < MIN:
				curPos = MAX
			if (curPos == 0):
				trueCount += 1

	print(f"{dir}{num}, {curPos}, {trueCount}")


print(trueCount)

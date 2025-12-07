#################################################################
###### https://adventofcode.com/2024/day/7 #######################
#################################################################
import numpy as np

# misc functions
def fprint(debug: str) -> str:
	print(debug)
	return debug + "\n"

def debugLog(debugString: str):
	fileLoc = ".\Day" + DAY_NO +"\misc\zdebug.txt"
	with open(fileLoc, "w") as fd:
		fd.writelines(debugString)

file = "input.txt"

DAY_NO = "7"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]
print(cleanInput)

width = len(cleanInput[0])
height = len(cleanInput)
print(f"Board dimensions {width}, {height}")

spliterBoard = np.zeros((height+1, width), dtype=str)
beamBoard = np.zeros((height+1, width), dtype=str)
print(spliterBoard)

emptyCell = " "
spliterCell = "^"
beamCell = "|"

for y in range(height):
	for x in range(width):
		if cleanInput[y][x] == "S":
			beamBoard[y][x] = beamCell
			spliterBoard[y][x] = emptyCell
		elif cleanInput[y][x] == spliterCell:
			spliterBoard[y][x] = spliterCell
			beamBoard[y][x] = emptyCell
		else:
			spliterBoard[y][x] = emptyCell
			beamBoard[y][x] = emptyCell
splitCount = 0
for y in range(height):
	for x in range(width):
		splitCellInfo = spliterBoard[y+1][x]
		beamCellInfo = beamBoard[y][x]

		if not (beamCellInfo == beamCell):
			continue

		if splitCellInfo == spliterCell:
			beamBoard[y+1][x+1] = beamCell
			beamBoard[y+1][x-1] = beamCell
			splitCount += 1
		else:
			beamBoard[y+1][x] = beamCell

print(splitCount)



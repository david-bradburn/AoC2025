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
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]
print(cleanInput)

width = len(cleanInput[0])
height = len(cleanInput)
print(f"Board dimensions {width}, {height}")

spliterBoard = np.zeros((height+1, width), dtype=str)
beamBoard = np.zeros((height+1, width), dtype=int)
print(spliterBoard)

emptyCell = " "
spliterCell = "^"
# beamCell = "|"

for y in range(height):
	for x in range(width):
		if cleanInput[y][x] == "S":
			beamBoard[y][x] = 1
			spliterBoard[y][x] = emptyCell
		elif cleanInput[y][x] == spliterCell:
			spliterBoard[y][x] = spliterCell
			beamBoard[y][x] = 0
		else:
			spliterBoard[y][x] = emptyCell
			beamBoard[y][x] = 0

# splitCount = 0
for y in range(height):
	for x in range(width):
		splitCellInfo = spliterBoard[y+1][x]
		beamCellInfo = beamBoard[y][x]
		# print(beamCellInfo)
		if (beamCellInfo == 0):
			continue

		if splitCellInfo == spliterCell:
			beamBoard[y+1][x+1] += beamCellInfo
			beamBoard[y+1][x-1] += beamCellInfo
		else:
			beamBoard[y+1][x] += beamCellInfo


for y in range(height):
	tmpstr = ""
	for x in range(width):
		splitCellInfo = spliterBoard[y][x]
		beamCellInfo = beamBoard[y][x]
		if beamCellInfo != 0:
			tmpstr += str(beamCellInfo)
		elif splitCellInfo == "^":
			tmpstr += "^"
		else:
			tmpstr += " "
	print(tmpstr)
# print(beamBoard)
count = 0

for x in beamBoard[height]:
	count += x

print(count)

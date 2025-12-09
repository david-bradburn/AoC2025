#################################################################
###### https://adventofcode.com/2024/day/9 ######################
#################################################################

# misc functions
def fprint(debug: str) -> str:
	print(debug)
	return debug + "\n"

def debugLog(debugString: str):
	fileLoc = ".\Day" + DAY_NO +"\misc\zdebug.txt"
	with open(fileLoc, "w") as fd:
		fd.writelines(debugString)

file = "input.txt"

DAY_NO = "9"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]

coords = []

for coord in cleanInput:
	x,y = coord.split(",")
	coords.append([int(x),int(y)])

print(coords)


def findArea(coord1: list, coord2: list):
	x1 =coord1[0]
	y1 =coord1[1]
	x2 =coord2[0]
	y2 =coord2[1]

	area = (abs(x1-x2)+1)*(abs(y2-y1)+1)
	return area

areas = []
for coordA in coords:
	for coordB in coords:
		areas.append(findArea(coordA, coordB))

print(max(areas))
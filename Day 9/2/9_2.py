#################################################################
###### https://adventofcode.com/2024/day/9 ######################
#################################################################

import matplotlib.pyplot as plt
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

DAY_NO = "9"
PART = "2"

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
xs = []
ys = []
for coord in coords:
	xs.append(coord[0])
	ys.append(coord[1])

plt.scatter(xs,ys)
plt.plot(xs,ys)
# plt.show()
# 1906,50085
# 2246,48699

# coord1 = [2246,48699]
# coord2 = [97437,43965]

top = [94967,50085]
bottom = [94967,48699]
i = [98162,50091]
xt = top[0]
yt = top[1]
for index, coord in enumerate(coords):
	if index == 0:
		xprev  = coord[0]
		yprev  = coord[1]
		continue
	xc = coord[0]
	yc = coord[1]


	if (((xprev < xt) and (xc > xt)) or ((xprev > xt) and (xc < xt))) and yc > yt:
		print(coord)

	xprev  = coord[0]
	yprev  = coord[1]

coord2 = [5633,67624]
print(findArea(top, coord2))




# 94967,50085
# 94967,48699
# areas = []
# for coordA in coords:
# 	for coordB in coords:
# 		areas.append(findArea(coordA, coordB))

# print(max(areas))

# 1559954980 too small
# 1377126080 too small
# 1309772046
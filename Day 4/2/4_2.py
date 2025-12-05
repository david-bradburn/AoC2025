#################################################################
###### https://adventofcode.com/2024/day/4 #######################
#################################################################
import numpy as np
file = "input.txt"

DAY_NO = "4"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]

print(cleanInput)

length = len(cleanInput[0])
height = len(cleanInput)

print(f"{length}, {height}")
wall = np.zeros((length+2, height+2), dtype=int)

print(wall)
for y in range(1,height+1):
	for x in range(1, length+1):
		if cleanInput[y-1][x-1] == "@":
			wall[y][x] = 1

print(wall)

def returnCount3x3(arr, y, x):
	return arr[y-1][x-1] + arr[y-1][x] + arr[y-1][x+1] + arr[y][x-1] + arr[y][x+1] + arr[y+1][x-1] + arr[y+1][x] + arr[y+1][x+1]

lastcount = -1
count = 0
while lastcount != count:
	lastcount = count
	for y in range(1,height+1):
		for x in range(1, length+1):
			# print(f"{x},{y}, {returnCount3x3(wall, y, x)}, {returnCount3x3(wall, y, x) < 4}")
			if wall[y][x]*(returnCount3x3(wall, y, x) < 4):
				wall[y][x] = 0
				count += 1
	print(count)


print(count)

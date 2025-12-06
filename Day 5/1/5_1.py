#################################################################
###### https://adventofcode.com/2024/day/5 #######################
#################################################################

file = "input.txt"

DAY_NO = "5"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

ranges = []
idList = []

blanklineSeen = False

for line in rawInput:
	if(not blanklineSeen):
		# print(len(line))
		if len(line) == 1:
			blanklineSeen = True
			continue
		cleanline = line.strip("\n")
		# print(cleanline)

		splitline = cleanline.split("-")
		# print(splitline)
		lower, higher = splitline[0], splitline[1]
		ranges.append([int(lower), int(higher)])

	else:
		idList.append(int(line.strip("\n")))

print(ranges)
print(idList)

def checkInRange(FreshIDS, ID):
	count = 0
	for ranges in FreshIDS:
		lower = ranges[0]
		upper = ranges[1]
		# print(type(lower), type(upper))
		# print(type(ID))
		assert(lower <= upper)
		if (ID >= lower) and (ID <= upper):
			count += 1

	return count


total = 0
for ID in idList:
	res = checkInRange(ranges, ID)
	if res > 0:
		total += 1

print(total)

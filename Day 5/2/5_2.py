#################################################################
###### https://adventofcode.com/2024/day/5 #######################
#################################################################

file = "input.txt"

DAY_NO = "5"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

ranges = []

blanklineSeen = False

for line in rawInput:
	if(not blanklineSeen):
		# print(len(line))
		if len(line) == 1:
			blanklineSeen = True
			break
		cleanline = line.strip("\n")
		# print(cleanline)

		splitline = cleanline.split("-")
		# print(splitline)
		lower, higher = splitline[0], splitline[1]
		ranges.append([int(lower), int(higher)])

print(ranges)

#rip can't do dumb methood wahh

def fprint(debug: str):
	print(debug)
	return debug + "\n"


def checkInRange(FreshIDS):
	tck = False
	# count = 0
	checkedRanges = []
	resultsDebug = ""

	for ranges in FreshIDS:
		resultsDebug += fprint("---------------------------------------------------------------------------------------")
		lower = ranges[0]
		upper = ranges[1]
		delta = upper - lower + 1 # inclusive
		resultsDebug += fprint(f"{lower}, {upper}, {delta}")

		if checkedRanges == []:
			assert(not tck)
			tck = True
			checkedRanges.append([lower, upper])
		else:

			for cRanges in checkedRanges:#
				assert (lower <= upper)
				upperbelowLower = upper < cRanges[0]
				lowerAboveUpper = lower > cRanges[1]

				lowerContained = (not lowerAboveUpper) and (lower >= cRanges[0])
				upperContained = (not upperbelowLower) and (upper <= cRanges[1])


				fullyContained = lowerContained and upperContained

				upperaboveupper = upper > cRanges[1]
				lowerbelowlower = lower < cRanges[0]

				containsCRanges = upperaboveupper and lowerbelowlower

				if fullyContained:
					resultsDebug += fprint(f"lower: {lower}, upper: {upper} is in {cRanges} fully")
					break
				elif containsCRanges:
					# i hate this case
					lower0 = lower
					upper0 = cRanges [0] - 1

					lower1 = cRanges [1] +1
					upper1 = upper
					FreshIDS.append([lower0, upper0])
					FreshIDS.append([lower1, upper1])

					break
				elif lowerContained:
					resultsDebug += fprint(f"lower: {lower} is above {cRanges[0]}, {lower >= cRanges[0]}  but upper: {upper} is above {cRanges[1]}, {upper > cRanges[1]} ")
					resultsDebug += fprint(f"lower update: {lower} -> {cRanges[1] + 1}")
					lower = cRanges[1] + 1
				elif upperContained:
					resultsDebug += fprint(f"upper: {upper} is below {cRanges[1]}, {upper <= cRanges[1]}  but upper: {lower} is below {cRanges[0]}, {lower < cRanges[0]} ")
					resultsDebug += fprint(f"upper update: {upper} -> {cRanges[0] - 1}")
					upper = cRanges[0] - 1
				elif upperbelowLower or lowerAboveUpper:
					assert(upperbelowLower ^ lowerAboveUpper)
					resultsDebug += fprint(f"lower: {lower}, upper: {upper} is outside {cRanges} fully, {(lower > cRanges[1]) ^ (upper < cRanges[0]) }")
					continue
				else:
					Exception("What")
			else:
				resultsDebug += fprint(f"range ({lower, upper}) is valid and will be added to checkedRanges {checkedRanges}")
				checkedRanges.append([lower, upper])







	return checkedRanges, resultsDebug


def totalupRanges(arr):
	count = 0
	for ranges in arr:
		count += ranges[1] - ranges[0] + 1

	return count


res, temp = checkInRange(ranges)

with open(f".\Day {DAY_NO}\misc\zdebug.txt", "w") as fd:
	fd.writelines(temp)

total = totalupRanges(res)


print(total)

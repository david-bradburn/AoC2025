#################################################################
###### https://adventofcode.com/2024/day/2 #######################
#################################################################

import math

file = "input.txt"

DAY_NO = "2"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = rawInput[0].strip("\n")
splitInput = cleanInput.split(",")

data = [i.split("-") for i in splitInput]

print (data)



def isInvalid(lower: int, upper: int):
	sum = 0
	for number in range(lower, upper+1):
		strnumber = str(number)
		lenNumber = len(strnumber)
		# if lenNumber == 1:
		# 	continue

		# print(f"number: {number}")

		for lenSlice in range(1 ,math.floor(lenNumber/2)+1):
			# print(f"Try slice lenth: {lenSlice}")
			if (lenNumber % lenSlice) == 0:
				# print(f"Valid slice length: {lenSlice}")
				numberOfSlices = int(lenNumber/lenSlice)
				# print(f"Number of slices: {numberOfSlices}")

				assert(numberOfSlices == lenNumber/lenSlice)
				slice = strnumber[0:lenSlice]
				for sliceIndex in range(1,numberOfSlices):
					if slice != strnumber[sliceIndex*lenSlice:(sliceIndex+1)*lenSlice]:
						break
				else:
					# print(f"Invalid ID: {strnumber}")
					sum += number
					break

	return sum


total = 0#

index = 1
for FID, LID in data:
	print("------------------")
	print(FID, LID, index)
	index += 1
	total += isInvalid(int(FID), int(LID))

	print(total)

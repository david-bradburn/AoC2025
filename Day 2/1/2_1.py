#################################################################
###### https://adventofcode.com/2024/day/2 #######################
#################################################################

file = "input.txt"

DAY_NO = "2"
PART = "1"

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
		if lenNumber % 2 == 1:
			continue
		else:
			if strnumber[:int(lenNumber/2)] == strnumber[int(lenNumber/2):]:
				print(strnumber)
				sum += number

	return sum


total = 0
for FID, LID in data:
	print(FID, LID)
	total += isInvalid(int(FID), int(LID))

	print(total)

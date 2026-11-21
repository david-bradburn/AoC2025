#################################################################
###### https://adventofcode.com/2024/day/11 #######################
#################################################################

# misc functions
def fprint(debug: str) -> str:
	print(debug)
	return debug + "\n"

def debugLog(debugString: str):
	fileLoc = ".\Day" + DAY_NO +"\misc\zdebug.txt"
	with open(fileLoc, "w") as fd:
		fd.writelines(debugString)

file = "test.txt"

DAY_NO = "11"
PART = "1"

welcome_msg = "AoC 2024 Day " + DAY_NO + " Part " + PART
print(welcome_msg)

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()
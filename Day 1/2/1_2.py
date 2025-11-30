#################################################################
###### https://adventofcode.com/2024/day/1 #######################
#################################################################

file = "test.txt"

DAY_NO = "1"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()
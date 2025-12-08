#################################################################
###### https://adventofcode.com/2024/day/8 ######################
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

DAY_NO = "8"
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanInput = [n.strip("\n") for n in rawInput]
coord_dict = {}
for index, element in enumerate(cleanInput):
	splitEle = element.split(",")
	coord_dict[index] = [int(splitEle[0]), int(splitEle[1]), int(splitEle[2])]

# print(coord_dict)
#data as x,y,z

circuit_dict = {}

def straightLineDistance(coord1: list, coord2: list) -> int:
	x1 = coord1[0]
	y1 = coord1[1]
	z1 = coord1[2]
	x2 = coord2[0]
	y2 = coord2[1]
	z2 = coord2[2]

	return (abs(x1-x2)**2 + abs(y1-y2)**2 + abs(z1-z2)**2)**(1/2)


def determine_distances(coords: dict):
	distance_dict = {}
	tempDict = coords.copy()
	for key in coords:
		print(len(coords))
		junctioncoords = coords[key]
		print(f"ID: {key}, coords: {junctioncoords}")
		tempDict.pop(key)
		for remainingKey in tempDict:
			# print(key, remainingKey)
			otherJunctionCoords = tempDict[remainingKey]
			dist = straightLineDistance(junctioncoords, otherJunctionCoords)
			if dist in distance_dict:
				Exception("Uh oh")
			else:
				distance_dict[dist] = [key, remainingKey]

	sorted_distance_dict = dict(sorted(distance_dict.items()))
	# print(sorted_distance_dict)
	return sorted_distance_dict


	# print(coord)

sorted_distance_dict = determine_distances(coord_dict)
# 24.3: [0 2]
# 30.4: [0 3]


class tree():
	def __init__(self, sorted_distance_dict, coord_dict):
		self.coord_dict = coord_dict
		self.sorted_distance_dict = sorted_distance_dict
		self.circuits = []
		self.maxcons = 10

		self.main()


	def checkInCircuit(self, ids: list):
		if self.circuits == []:
			self.circuits.append(ids)
		else:
			id1 = ids[0]
			id2 = ids[1]

			id1_index = ""
			id2_index = ""
			for index, circuit in enumerate(self.circuits):
				if (id1 in circuit) and (not (id2 in circuit)):
					print(f"id {id1} in circuit {index} : {circuit}")
					# self.circuits[index].append(id2)
					id1_index = index

				elif (not (id1 in circuit)) and ((id2 in circuit)):
					print(f"id {id2} in circuit {index} : {circuit}")
					# self.circuits[index].append(id1)
					id2_index = index

				elif (id1 in circuit) and (id2 in circuit):
					print(f"id {id1} and {id2} in circuit {index} : {circuit}")
					id1_index = index
					id2_index = index

			if (id1_index == "") and (id2_index == ""):
				self.circuits.append([id1, id2])

			elif (not (id1_index == "")) and (id2_index == ""):
				self.circuits[id1_index].append(id2)
			elif (id1_index == "") and (not (id2_index == "")):
				self.circuits[id2_index].append(id1)
			elif(not (id1_index == "")) and (not (id2_index == "")) and (id1_index != id2_index):
				print(id2_index, id1_index)
				min_index = min(id1_index,id2_index)
				max_index = max(id1_index,id2_index)
				# print(self.circuits[id2_index])
				circuit2 = self.circuits.pop(max_index)
				print(f"cir: {circuit2}")
				for ele in circuit2:
					self.circuits[min_index].append(ele)
			else:
				Exception("shit")


	def main(self):
		for i in range(self.maxcons):
			print("-----------")

			print(f"Connection {i+1}")
			minDistance = list(self.sorted_distance_dict)[0]
			print(f"min distance: {minDistance}")
			ids = self.sorted_distance_dict[minDistance]
			print(f"ids: {ids}")
			self.checkInCircuit(ids)
			self.sorted_distance_dict.pop(minDistance)
			# print(f"circuits :{self.circuits}")
			print(self.circuits)

		tmpLengths = []
		for ele in self.circuits:
			tmpLengths.append(len(ele))

		sortedList = sorted(tmpLengths)
		print(sortedList)
		mul = 1
		for i in range(3):
			mul *= sortedList[-(i+1)]

		print(mul)





p1 = tree(sorted_distance_dict, coord_dict)


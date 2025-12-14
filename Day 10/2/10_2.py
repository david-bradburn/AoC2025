#################################################################
###### https://adventofcode.com/2025/day/10 #####################
#################################################################
import ast

import copy

# misc functions
def fprint(debug: str) -> str:
	print(debug)
	return debug + "\n"

def debugLog(debugString: str):
	fileLoc = ".\Day" + DAY_NO +"\misc\zdebug.txt"
	with open(fileLoc, "w") as fd:
		fd.writelines(debugString)

file = "input.txt"

DAY_NO = "10"
PART = "2"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [n.strip("\n") for n in rawInput]

machine = []

for line in cleanerInput:
	temp = line.split(" ")
	# buttonsCount = len(temp) - 2
	# lights = temp[0][1:-1]
	joltage = temp[-1][1:-1].split(",")
	buttons =temp[1:-1] # [n[1:-1].split(",") for n in temp[1:-1]]

	# lightsInt = ''
	# for light in lights:
	# 	lightsInt += str(1 if light == '#' else 0)
	buttonsClean = []
	for button in buttons:
		buttonsStripped = button[1:-1].split(",")
		temp = []
		for lightButton in buttonsStripped:
			temp.append(int(lightButton))
		buttonsClean.append(temp)

	joltageClean = []
	for value in joltage:
		# print(value)
		joltageClean.append(int(value))

	# print(lightsInt)
	# print(lights, buttonsClean, joltage)


	machine.append([buttonsClean, joltageClean])

for i in machine:
	print(i)
# print('0'*4)
class pathFinding():
	def __init__(self, joltage, buttons):
		self.targetjoltage = joltage
		self.joltageSize = len(joltage)
		# print(f"num joltages: {self.joltageSize}")
		# self.numStates = 2**self.stateSize
		self.STARTSTATE = [0]*self.joltageSize
		self.buttons = buttons
		self.numButtons = len(self.buttons)
		self.calculateMaxButtonPresses()

		buttonPressCount = [0]*self.numButtons
		# print(self.STARTSTATE)
		self.stateDict = {f"{self.STARTSTATE}": [0, self.hueristic(self.STARTSTATE, self.targetjoltage), buttonPressCount, None]}


		self.openList = {f"{self.STARTSTATE}": [0, self.hueristic(self.STARTSTATE, self.targetjoltage), buttonPressCount, None]}
		self.closedList = []


		self.main()

		# print(self.stateDict)
	def calculateMaxButtonPresses(self):
		self.maxButtonPress = []
		for button in self.buttons:
			tmp = [0]*self.joltageSize
			count = 0
			while self.isValid(tmp, [], False):
				count += 1
				tmp = self.pressButton(tmp, button)

			self.maxButtonPress.append(count)
		print(self.maxButtonPress)


	def finalCount(self):
		return self.stateDict[f"{self.targetjoltage}"][0]

	def pressButton(self, state:str, button:list):
		prevState = state
		curState = state # should be in binary form
		if type(curState) == str:
			curState = ast.literal_eval(curState)

		for light in button:
			curState[light] += 1

		return curState

	def isValid(self, curState, buttonPressCount, mask:bool):
		for index, state in enumerate(curState):
			if state > self.targetjoltage[index]:
				return False

		if mask:
			for index, count in enumerate(buttonPressCount):
				if count > self.maxButtonPress[index]:
					return False
		return True

	def hueristic(self, pos1, pos2):
		dis = 0
		for index, state in enumerate(pos1):
			dis += (state - pos2[index])**2
		dis = dis**(1/2)
		return dis




	def main(self):
		while self.openList:
			# print(len(self.openList))
			pos = list(self.openList)[0]
			posList = ast.literal_eval(pos)
			curPosHuer_g = self.openList[pos][0]
			print(curPosHuer_g)
			curf = self.openList[pos][1]
			# print(self.hueristic(posList, self.targetjoltage))

			if pos == self.targetjoltage:
				break

			posEnd = list(self.openList)[-1]

			buttonPressCount = self.openList[pos][2]

			self.closedList.append(pos)
			self.openList.pop(pos)

			# self.hueristic(posList)

			# countPresses = self.stateDict[pos][0]

			for buttonIndex, button in enumerate(self.buttons):
				tmpCount = copy.deepcopy(buttonPressCount)
				tmpCount[buttonIndex] += 1
				newStateList = self.pressButton(pos, button)

				qValid  = self.isValid(newStateList, tmpCount, True)
				if not qValid:
					continue

				newState = str(newStateList)
				# print(newState)
				if newState in self.closedList:
					continue

				ten_g = curPosHuer_g + 1

				if newState not in self.openList:
					self.openList[newState] = [ten_g, ten_g+self.hueristic(newStateList, self.targetjoltage), tmpCount, pos]
					self.stateDict[newState] = [ten_g, ten_g+self.hueristic(newStateList, self.targetjoltage), tmpCount, pos]
				elif ten_g > self.openList[newState][0]:
					continue
				else:
					self.openList[newState] = [ten_g, ten_g+self.hueristic(newStateList, self.targetjoltage), tmpCount, pos]
					self.stateDict[newState] = [ten_g, ten_g+self.hueristic(newStateList, self.targetjoltage), tmpCount, pos]



			sorted_dict = {k: v for k, v in sorted(self.openList.items(), key=lambda item: item[1][1])}


			self.openList = sorted_dict





class ahh():
	def __init__(self, machine):
		self.data = machine
		# print(f"lights: {self.lights}")
		# print(self.buttons)
		total = 0
		for indexMachine, machine in enumerate(self.data):
			print("--------------------------------------")
			print(f"machine Index: {indexMachine}")
			# self.lights = machine[0]
			self.buttons = machine[0]
			self.joltage = machine[1]
			tmp = pathFinding(self.joltage, self.buttons)
			total += tmp.finalCount()
		print(total)




# this is basically a hidden path finding algorithm


p2 = ahh(machine)

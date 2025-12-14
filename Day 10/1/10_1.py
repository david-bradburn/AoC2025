#################################################################
###### https://adventofcode.com/2025/day/10 #######################
#################################################################

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
PART = "1"

file_path_base = "Day " + DAY_NO + "/misc/"

with open(file_path_base + file, "r") as fd:
	rawInput = fd.readlines()

cleanerInput = [n.strip("\n") for n in rawInput]

machine = []

for line in cleanerInput:
	temp = line.split(" ")
	buttonsCount = len(temp) - 2
	lights = temp[0][1:-1]
	joltage = temp[-1]
	buttons =temp[1:-1] # [n[1:-1].split(",") for n in temp[1:-1]]

	lightsInt = ''
	for light in lights:
		lightsInt += str(1 if light == '#' else 0)
	buttonsClean = []
	for button in buttons:
		# print(button)
		buttonsStripped = button[1:-1].split(",")
		temp = []
		for lightButton in buttonsStripped:
			temp.append(int(lightButton))
		buttonsClean.append(temp)
	# print(lightsInt)
	# print(lights, buttonsClean, joltage)


	machine.append([lightsInt, buttonsClean, joltage])

# print('0'*4)
class pathFinding():
	def __init__(self, state, buttons):
		self.targetState = state
		self.stateSize = len(state)
		print(f"num state: {self.stateSize}")
		self.numStates = 2**self.stateSize
		self.STARTSTATE = '0'*self.stateSize
		self.stateDict = {self.STARTSTATE: 0}

		self.buttons = buttons
		self.numButtons = len(self.buttons)


		self.queue = {self.STARTSTATE: 0}

		self.main()

		print(self.stateDict)

	def finalCount(self):
		return self.stateDict[self.targetState]

	def pressButton(self, state:str, button:list):
		prevState = state
		curState = state # should be in binary form
		# print(f"current state: {curState}")
		# print(button)
		for light in button:
			# print(light, type(light))
			oneHotButtonStr = '1' + ('0'*(self.stateSize -1 - light))
			curState = f'{(int(curState, 2) ^ int(oneHotButtonStr, 2)):0{self.stateSize}b}'
		# print(curState, prevState)

		return curState

	def main(self):
		while self.queue:
			pos = list(self.queue)[0]
			countPresses = self.stateDict[pos]
			for button in self.buttons:
				newState = self.pressButton(pos, button)
				if newState in self.stateDict:
					if (countPresses + 1) < self.stateDict[newState]:
						self.stateDict[newState] = countPresses + 1
						self.queue[newState] = countPresses + 1
				else:
					self.stateDict[newState] = countPresses + 1
					self.queue[newState] = countPresses + 1


			self.queue.pop(pos)

			sorted_dict = {}

			for key in sorted(self.queue, key=self.queue.get):
					sorted_dict[key] = self.queue[key]

			self.queue = sorted_dict





class ahh():
	def __init__(self, machine):
		self.data = machine
		# print(f"lights: {self.lights}")
		# print(self.buttons)
		total = 0
		for machine in self.data:
			print("--------------------------------------")
			self.lights = machine[0]
			self.buttons = machine[1]
			tmp = pathFinding(self.lights, self.buttons)
			total += tmp.finalCount()
		print(total)




# this is basically a hidden path finding algorithm


p1 = ahh(machine)

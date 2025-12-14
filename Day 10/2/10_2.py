#################################################################
###### https://adventofcode.com/2025/day/10 #####################
#################################################################
import ast

import copy
import numpy as np
from itertools import product

# misc functions
def fprint(debug: str) -> str:
	print(debug)
	return debug + "\n"

def debugLog(debugString: str):
	fileLoc = ".\Day" + DAY_NO +"\misc\zdebug.txt"
	with open(fileLoc, "w") as fd:
		fd.writelines(debugString)

file = "test.txt"

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


	machine.append([buttonsClean, joltageClean])

for i in machine:
	print(i)





class pathFinding():
	def __init__(self, joltage, buttons):
		self.targetjoltage = joltage
		self.targetj = np.array(self.targetjoltage).transpose()
		print(f"egg {self.targetj}, {self.targetj.shape}")
		self.joltageSize = len(joltage)

		assert(self.joltageSize >= 4 and self.joltageSize <= 10)
		self.STARTSTATE = [0]*self.joltageSize
		self.buttons = buttons
		self.numButtons = len(self.buttons)
		self.calculateMaxButtonPresses() # sets self.maxbutttonspresses


		self.numberofCombos = self.multArr(self.maxButtonPress)
		print(self.numberofCombos)
		self.STARTSTATEVEC = np.array(self.STARTSTATE)

		self.buttonVecs = self.buttonsToStateTrans()
		print(self.buttonVecs)
		A = np.array(self.buttonVecs)
		At = A.transpose()
		np.matmul

		try:
			p1 = np.matmul(At,A)**(np.matmul(-At,self.targetj))
			print(p1)
		except:
			p2 = np.linalg.matrix_power(np.matmul(At, np.matmul(A, At)),(-self.targetj))


		# self.main()

		# print(self.stateDict)
	def calculateMaxButtonPresses(self):
		self.maxButtonPress = []
		for button in self.buttons:
			tmp = [0]*self.joltageSize
			count = 0
			while self.isValid(tmp, []):
				count += 1
				tmp = self.pressButton(tmp, button)

			self.maxButtonPress.append(count)
		print(self.maxButtonPress)


	def finalCount(self):
		print(f"number of buttons pressed: {self.pressCount}")
		return min(self.pressCount)
		# return self.stateDict[f"{self.targetjoltage}"][0]

	def pressButton(self, state:str, button:list):
		prevState = state
		curState = state # should be in binary form
		if type(curState) == str:
			curState = ast.literal_eval(curState)

		for light in button:
			curState[light] += 1

		return curState

	def isValid(self, curState, buttonPressCount):
		for index, state in enumerate(curState):
			if state > self.targetjoltage[index]:
				return False

		return True


	def buttonsToStateTrans(self):
		temp = []
		for buttton in self.buttons:
			tmp = copy.deepcopy(self.STARTSTATE)
			for index in buttton:
				tmp[index] += 1
			# print(tmp)

			temp.append(tmp)
		# print(temp)
		return temp

	def checkFunction(self, presses):
		value = copy.deepcopy(self.STARTSTATEVEC)
		# print(presses)
		# print(len(presses), self.numButtons, len(presses) == self.numButtons)
		if (len(presses) == self.numButtons):
			assert(len(presses) == self.numButtons)
			assert(len(presses) == len(self.buttonVecs))
			# print(value)
			# print(self.buttonVecs)
			for index in range(self.numButtons):

				value += self.buttonVecs[index]*int(presses[index])
			if list(value) == self.targetjoltage:
				self.pressCount.append(self.countPressed(presses))

	def multArr(self, arr):
		i = 1
		for n in arr:
			i *= n
		return i
	def countPressed(self, pressses):
		total = 0
		for value in pressses:
			total += value
		return total

	def main(self):
		self.pressCount = []
		print(f"Number of buttons: {self.numButtons}") ## should be the number of 4 loops
		stateList = [range(n + 1) for n in self.maxButtonPress]

		for presses in product(*stateList):
			# print(presses[0]/self.maxButtonPress[0])
			self.checkFunction(presses)





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

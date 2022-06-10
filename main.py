#Made by Alex

#======Libraries======

#======Functions======
#Subtraction Function
def sub(l, start, end):
	for i in range(start, end):
		#Detects
		if l[i] == "-":
			temp = 0
			for j in range(i, len(l)):
				#Counts
				if l[j] == "-":
					temp += 1
				#Stops
				elif isinstance(l[j], float):
					break
			#Negates Number
			if temp % 2 == 1:
				l[j] *= -1
			#Pops
			for k in range(i, j):
				l.pop(i)
			#Fail-safe
			if isinstance(l[i - 1], float):
				l.insert(i, "+")
			break

#Multiplication & Division Function
def multidiv(l, start, end):
	for i in range(start, end):
		#Detects
		if l[i] == "*":
			#Multiplies Number
			l[i - 1] *= l[i + 1]
			#Pops
			l.pop(i), l.pop(i)
			break
		#Detects
		elif l[i] == "/":
			#Divides Number
			l[i - 1] /= l[i + 1]
			#Pops
			l.pop(i), l.pop(i)
			break

#Addition Function
def add(l, start, end):
	for i in range(start, end):
		#Detects
		if l[i] == "+":
			#Adds Number
			l[i - 1] += l[i + 1]
			#Pops
			l.pop(i), l.pop(i)
			break

#======Main======
def main():
	#Stored Answer
	ans = 0
	#While Loop
	while True:
		#Reset Variable
		reset = 0
		#Expression Input
		l, operations = input("Expression: "), ["+", "-", "*", "/"]
		if l.lower() == "stop":
			return print("Stopping the calculator.")
		l = l.replace(" ", "" , -1) # Removes all whitespace
		for i in operations:
			l = l.replace(i, f" {i} ", -1) # Adds 1 space before and after operations
		l = list(l.split())
		print(l)
		#Parsers Elements To Float
		for i in range(len(l)):
			try:
				l[i] = float(l[i])
			except ValueError:
				#Invalid Input
				if l[i] not in operations:
					#Stops The Program
					if "stop" in l[i].lower():
						return print("Stopping the calculator.")
					#Stored Answer
					if "ans" in l[i].lower():
						l[i] = ans
					#Invalid Input
					else:
						temp = []
						for j in range(len(l)):
							if l[j] not in operations and not isinstance(l[j], float):
								temp.append(l[j])
						print("Invalid inputs:", *temp)
						reset = 1
						break
				else:
					pass
		#Reset
		if reset == 1:
			continue
		#Automatic Stored Answer
		if not isinstance(l[0], float):
			l.insert(0, ans)

		#Calculation
		while "-" in l:
			sub(l, 0, len(l) - 1)
		while "*" in l or "/" in l:
			multidiv(l, 0, len(l) - 1)
		while "+" in l:
			add(l, 0, len(l) - 1)
		print("Result:", l[0])
		ans = l[0]

#======Execution Check======
if __name__ == '__main__':
	print("Running the calculator. Type \"STOP\" to exit.")
	main()
	input() # Does not automatically close
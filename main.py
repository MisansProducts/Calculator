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
	ans = 0 # Stored answer
	while True:
		reset = False #Reset variable

		#Expression input
		l, operations = input("Expression: "), ["+", "-", "*", "/"]

		#Exit function
		if l.lower() == "stop":
			return print("Stopping the calculator.")
		
		#Removes all whitespace
		l = l.replace(" ", "" , -1)

		#Splits the input string by its operators and operands then converts it to a list data type
		for operator in operations:
			l = l.replace(operator, f" {operator} ", -1) #Adds 1 space before and after operations
		l = list(l.split())

		print(l) #Shows the list

		#Goes through each element in the list
		invalid = [] #Invalid inputs
		for i in range(len(l)):
			try:
				l[i] = float(l[i]) #Parse element to float
			except ValueError:
				if l[i] not in operations:
					#Stored answer
					if "ans" in l[i].lower():
						l[i] = ans
					#Invalid input
					else:
						invalid.append(l[i]) #Adds invalid inputs to list
						reset = True #Restarts the calculator
				else:
					pass
		#Reset
		if reset:
			print("Invalid inputs:", end = ' ')
			print(*invalid, sep = ', ', end = '\n')
			continue
		#Automatic stored answer
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
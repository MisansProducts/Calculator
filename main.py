#Made by Alex

#======Libraries======

#======Functions======
#Grouping Symbols Function
def group(l, start, end):
	oLast = start
	cFirst = start
	newL = [] #New expression inside grouping symbols
	groupError = True #In case grouping symbols are wrong way around (i.e. 4)+(3)
	for i in range(start, end):
		#We want to get the indices of the last open gSymbol and the first closed gSymbol
		if l[i] == "(":
			oLast = i #Gets last open gSymbol index
			if cFirst != start:
				break #Breaks if there is a grouping error
			groupError = False
		elif l[i] == ")":
			cFirst = i #Gets first closed gSymbol index
			if not groupError:
				break #Would normally break except if there is a grouping error
	#Grouping error -> remove grouping symbols
	if groupError:
		l.pop(oLast)
		l.pop(cFirst)
		return
	#Safety in case first element is oLast (do not check for last element)
	if oLast != 0:
		#Assumes multiplication on the left hand side
		if isinstance(l[oLast - 1], float):
			l.insert(oLast, "*")
			#Adjusts indices
			oLast += 1
			cFirst += 1
	#Safety in case last element is cFirst (out of range error)
	if cFirst != len(l) - 1:
		#Assumes multiplication on the right hand side
		if isinstance(l[cFirst + 1], float):
			l.insert(cFirst + 1, "*")
	#Can be more efficient by doing 1 loop
	for i in range(oLast + 1, cFirst):
		newL.append(l[i])
	if len(newL) == 0: newL.append(float(0))
	#Semi-recursion
	l[oLast] = calc(newL)
	#Simplifies expression
	for i in range(oLast + 1, cFirst + 1):
		l.pop(oLast + 1)

#Subtraction Function
def sub(l, start, end):
	for i in range(start, end):
		#Detects
		if l[i] == "-":
			temp = 0 #Number of subtraction operations before a number (i.e. 3---3)
			for j in range(i, len(l)):
				#Counts
				if l[j] == "-":
					temp += 1
				#Stops
				elif isinstance(l[j], float):
					break
			#Negates Number
			if temp % 2 == 1:
				l[j] *= -1 #Accounts for number of subtraction operations (i.e. 3---3 = -3)
			#Pops
			for k in range(i, j):
				l.pop(i)
			#Fail-safe
			if (isinstance(l[i - 1], float)) and (i != 0):
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

#Calculation Function
def calc(expression):
	while "(" in expression:
		group(expression, 0, len(expression))
	while "-" in expression:
		sub(expression, 0, len(expression) - 1)
	while "*" in expression or "/" in expression:
		multidiv(expression, 0, len(expression) - 1)
	while "+" in expression:
		add(expression, 0, len(expression) - 1)
	return expression[0]

#======Main======
def main():
	ans = 0 # Stored answer
	while True:
		reset = False #Reset variable

		#Expression input
		l, operations = input("Expression: "), ("+", "-", "*", "/", "(", ")")

		#Exit function
		if l.lower() == "stop":
			return print("Stopping the calculator.")
		
		#Removes all whitespace
		l = l.replace(" ", "" , -1)

		#Splits the input string by its operators and operands then converts it to a list data type
		for operator in operations:
			l = l.replace(operator, f" {operator} ", -1) #Adds 1 space before and after operations
		l = list(l.split())

		#No expression error
		if len(l) == 0:
			print("Please enter an expression or type STOP.")
			continue

		#Goes through each element in the list
		invalid = [] #Invalid inputs
		dupeOps = False #Keeps track of duplicate operators (i.e. 3++4)
		for i in range(len(l)):
			try:
				l[i] = float(l[i]) #Parse element to float
				dupeOps = False
			except ValueError:
				#Is not an operator
				if l[i] not in operations:
					#Stored answer
					if "ans" in l[i].lower():
						l[i] = ans
					#Invalid input
					else:
						invalid.append(l[i]) #Adds invalid inputs to list
						reset = True #Restarts the calculator
				#Is a consecutive operator
				elif dupeOps:
					allowedSymbols = ("-", "(")
					#Is not in allowed symbols
					if l[i] not in allowedSymbols:
						invalid.append(l[i]) #Adds invalid inputs to list
						reset = True #Restarts the calculator
				#Is the last element in the list
				elif (l[i] == l[-1]) and (i == len(l) - 1):
					allowedSymbols = (")")
					#Is not in allowed symbols
					if l[i] not in allowedSymbols:
						invalid.append(l[i]) #Adds invalid inputs to list
						reset = True #Restarts the calculator
				#Is an operator
				else:
					allowedSymbols = (")")
					#Is not in allowed symbols
					if l[i] not in allowedSymbols:
						dupeOps = True
					pass
		#Reset
		if reset:
			print("Invalid inputs:", end = ' ')
			print(*invalid, sep = ', ', end = '\n')
			continue
		#Automatic stored answer
		if not isinstance(l[0], float):
			allowedSymbols = ("-", "(", ")")
			if l[0] not in allowedSymbols:
				l.insert(0, ans)
		#Fix grouping symbols
		oCount = l.count("(") #Open grouping symbol count
		cCount = l.count(")") #Closed grouping symbol count
		#Insert open grouping symbols at the beginning
		if oCount < cCount:
			for i in range(oCount, cCount):
				l.insert(0, "(")
		#Append closed grouping symbols
		elif cCount < oCount:
			for i in range(cCount, oCount):
				l.append(")")

		#Calculation
		ans = calc(l) #Stores answer

		#Prints result
		if ans.is_integer():
			print("Result:", int(ans))
		else:
			print("Result:", ans)

#======Execution Check======
if __name__ == '__main__':
	print("Running the calculator. Type \"STOP\" to exit.")
	main()
import random

in_data = ['c horn? no', 'c forced? no', 'c mixed sat? no', 'c clause length = 3', 'c', 'p cnf 8  4', '1 2 0', '3 -4 0', '-5 -6 0', '8 7 0']

def parseCNF(data):
	cnf = list()
	cnf.append(list())
	lastVar = 0

	for line in in_data:
		variables = line.split()
		if len(variables) != 0 and variables[0] not in ("p", "c"):
			for variable in variables:
				literal = int(variable)
				lastVar = max(lastVar, abs(literal))
				if literal == 0:
					cnf.append(list())
				else:
					cnf[-1].append(literal)

	assert len(cnf[-1]) == 0
	cnf.pop()
	return (cnf, lastVar)

def SAT2solver(clauses, varNo, noOfTries):
    # set all variables to false
    cnf_arr = [-1] * varNo
    sat = True
    for _ in range(noOfTries):
        sat = True
        for clause in clauses:
            var1 = clause[0]
            var2 = clause[1]
            # get both variables in a clause
            first = var1 * cnf_arr[abs(var1 - 1)]
            second = var2 * cnf_arr[abs(var2 - 1)]
            # checking for sat
            if (first < 1) and (second < 1):
                sat = False
                # clause is not sat
                # randomly choose 1 variable in the clause to flip sign
                n = random.randint(0, 1)
                if n == 0:
                    cnf_arr[abs(var1 - 1)] = 1
                else:
                    cnf_arr[abs(var2 - 1)] = 1
                break
    if sat:
        print ("satisfied")
        return cnf_arr
    else:
        print ("not sat / tired of flipping coins")
        return None

clauses, varNo = parseCNF(in_data)
print(SAT2solver(clauses, varNo, 3))


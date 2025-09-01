import definations as df # df.combn(n,r) = combination calculator, nCr
#df.fact(n) = product of first n natural numbers

print("For the equation (a + b)^n")
config = input("Type a if \"a\" is variable, \"b\" if b is variable, \"ab\" if both are variable or \"pass\" if none are variable: ")
n = int(input("Enter the power of the expression: "))
a = input("Enter first term: ")
b = input("Enter second term: ")

b4calc = ""
if config.lower() == "a":
    b = float(b)
    for i in range(n+1):  
        coeff = df.combn(n, i)
        pwr_a = n - i
        pwr_b = i
        term = f"{coeff*(b**pwr_b)}*{a}^{pwr_a}" if pwr_a > 0 else f"{coeff}"
        if pwr_b > 0 and pwr_b != 1:
            term += f"*{b**pwr_b}"
        b4calc += term + " + "
    b4calc = b4calc.strip(" + ")
    print(b4calc)
elif config.lower() == 'pass':
    a = float(a)
    b = float(b)
    soln = (a + b)**n
    print(soln)
elif config.lower() == "b":
    b = float(b)
    for i in range(n+1):  
        coeff = df.combn(n, i)
        pwr_a = i
        pwr_b = n - i
        term = ""
        if pwr_a > 0 and pwr_a != 1:
            term += f"*{a**pwr_a}"
        term = f"{coeff*(a**pwr_a)}*{b}^{pwr_b}" if pwr_b > 0 else f"{coeff}"
        b4calc += term + " + "
    b4calc = b4calc.strip(" + ")
    print(b4calc) 
elif config.lower() == "ab":
    for i in range(n+1):  
        coeff = df.combn(n, i)
        pwr_a = n - i
        pwr_b = i
        term = f"{coeff}*{a}^{pwr_a}*{b}^{pwr_b}"
        b4calc += term + " + "
    b4calc = b4calc.strip(" + ")
    print(b4calc)
else:
    print("Invalid Input!")

input("Press any key to exit...")



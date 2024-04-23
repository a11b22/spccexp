#code optimisation by constant folding

def constant_folding(code):
    folded_code = []
    for line in code:
        if '=' in line:
            var, expr = line.split('=')
            var = var.strip()
            try:
                result = eval(expr.strip(), {})
                folded_code.append(f"{var} = {result}")
            except:
                folded_code.append(line)
        else:
            folded_code.append(line)
    return folded_code

def constant_propagation(code):
    symbol_table = {}
    optimized_code = []
    for line in code:
        if '=' in line:
            var, expr = line.split('=')
            var = var.strip()
            if all(char.isdigit() or char == '.' for char in expr.strip()):
                symbol_table[var] = expr.strip()
            else:
                for key, value in symbol_table.items():
                    expr = expr.replace(key, value)
                optimized_code.append(f"{var} = {expr.strip()}")
        else:
            optimized_code.append(line)
    return optimized_code

# User input for the code
code = []
print("Enter your code line by line. Enter 'done' when finished.")
while True:
    line = input()
    if line.lower() == 'done':
        break
    code.append(line)

# Constant Propagation
print("\nConstant Propagation:")
optimized_code_propagation = constant_propagation(code)
for line in optimized_code_propagation:
    print(line)

# Constant Folding
print("Constant Folding:")
optimized_code_folding = constant_folding(optimized_code_propagation)
for line in optimized_code_folding:
    print(line)

'''
Expected output:
Enter your code line by line. Enter 'done' when finished.

a=5

b=10

c=a+b

d=c+15

done

Constant Propagation:

c = 5+10

d = c+15

Constant Folding:

C = 15

d = c+15

'''

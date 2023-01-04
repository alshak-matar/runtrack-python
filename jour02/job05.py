def calcule(num1, string, num2):

    if string == "+":
        return num1 + num2
    elif string == "-":
        return num1 - num2
    elif string == "*":
        return num1 * num2
    elif string == "/":
        return num1 / num2
    elif string == "%":
        return num1 % num2

print(calcule(54,"+",46))

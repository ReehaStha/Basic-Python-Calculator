#Building a calculator 
#Notes:
#X = First Number
#O = Operation
#Y = Second Number
#It will work properly

def get_input():
    x = input("x: ")
    o = input("o: ")
    y = input("y: ")

    result = {"x": x, "o": o, "y": y}
    return result

def conditions(x, o, y):
    if o == "+":
        value = float(x) + float(y)
        result = print(value)

    elif o == "-":
        value = float(x) - float(y)
        result = print(value)

    elif o == "*":
        value = float(x) * float(y)
        result = print(value)

    elif o == "/":
        value = float(x) / float(y)
        result = print(value)

    else:
        result = print("You have entered wrong operation .... Error")

    return conditions

inputs = get_input()
result = conditions(inputs["x"], inputs["o"], inputs["y"])
print(result)

#Hope you like the code.............
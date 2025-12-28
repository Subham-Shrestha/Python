num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
oper = str(input("Enter operators (+, -, *, /) : "))
if (oper == "+"):
    sum = num1 + num2
    print("The sum of  " + " " + str(num1) + "&" + " " + str(num2) + " " + "is" + " " + str(sum))
elif (oper == "-"):
    diff = num1 - num2
    print("The difference of " + " " + str(num1)  + "&" + str(num2) + " " + "is" + ' ' + str(diff))
elif (oper == "*") :
    prod = num1 * num2
    print("The product of " + " " + str(num1) + "&" + str(num2) + "is" + " " + str(prod))
elif (oper == "/") : 
    divis = num1 / num2
    print("The division of " + " " + str(num1) + " " + str(num2) + " " + "is" + str(divis))
else :
    print("Invalid operator.")
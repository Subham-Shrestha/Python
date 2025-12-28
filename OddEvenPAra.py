# write a function that takes a number as a parameter and returns true if the number is even and false if the number is odd.

def checkEven(numbers):
    if numbers % 2 == 0:
        return True
    else:
        return False
b = checkEven(int(input("Enter a number : ")))
print(b)

# write a function that takes number as a parameter and prints whether the given number is odd or even.

def Para(num):
    if num % 2 == 0:
        return(f' {num} is even.')
    else :
        return(f' {num} is odd.')
a = Para(int(input("Enter a number : ")))
print(a)

# write a function that takes number and print even number upto that number.

def Func(number):
    return print(list(range(2, number, 2)))
a = Func(int(input("Enter a number : ")))